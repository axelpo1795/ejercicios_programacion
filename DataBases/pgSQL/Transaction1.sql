
BEGIN;

SET LOCAL search_path TO "BillsSchema", pg_temp;

DO $$
DECLARE
    v_user_id INTEGER := 1;
    v_bill_id INTEGER;
    v_total DOUBLE PRECISION;
    v_product RECORD;
BEGIN

    -- 1. Crear lista de productos a comprar
    CREATE TEMP TABLE purchase_items (
        product_id INTEGER,
        quantity INTEGER
    ) ON COMMIT DROP;

    INSERT INTO purchase_items (product_id, quantity)
    VALUES
        (1, 2),  -- 2 teclados
        (2, 3),  -- 3 mouse
        (3, 1);  -- 1 monitor

    -- 2. Verificar que el usuario existe
    IF NOT EXISTS (
        SELECT 1
        FROM "Users"
        WHERE "UserID" = v_user_id
    ) THEN
        RAISE EXCEPTION
            'El usuario % no existe', v_user_id;
    END IF;

    -- 3. Validar que existan productos en la compra
    IF NOT EXISTS (
        SELECT 1 FROM purchase_items
    ) THEN
        RAISE EXCEPTION
            'La compra no contiene productos';
    END IF;

    -- 4. Validar productos y cantidades
    IF EXISTS (
        SELECT 1
        FROM purchase_items i
        LEFT JOIN "Products" p
            ON p."ProductID" = i.product_id
        WHERE p."ProductID" IS NULL
           OR i.quantity IS NULL
           OR i.quantity <= 0
    ) THEN
        RAISE EXCEPTION
            'Producto inexistente o cantidad invalida';
    END IF;

    -- 5. Comprobar existencias y bloquear productos
    FOR v_product IN
        SELECT
            p."ProductID" AS product_id,
            p."Stock" AS stock,
            i.quantity
        FROM "Products" p
        JOIN (
            SELECT
                product_id,
                SUM(quantity) AS quantity
            FROM purchase_items
            GROUP BY product_id
        ) i ON p."ProductID" = i.product_id
        ORDER BY p."ProductID"
        FOR UPDATE OF p
    LOOP
        IF v_product.stock IS NULL
           OR v_product.stock < v_product.quantity THEN

            RAISE EXCEPTION
                'Stock insuficiente para producto %. Disponible: %, Solicitado: %',
                v_product.product_id,
                v_product.stock,
                v_product.quantity;
        END IF;
    END LOOP;

    -- 6. Calcular el total de la factura
    SELECT SUM(p."Price" * i.quantity)
    INTO v_total
    FROM "Products" p
    JOIN purchase_items i
        ON p."ProductID" = i.product_id;

    IF v_total IS NULL THEN
        RAISE EXCEPTION
            'No se pudo calcular el total';
    END IF;

    -- 7. Bloquear tabla para generar IDs manuales
    -- Evita IDs duplicados entre compras simultaneas
    LOCK TABLE "Bills", "BillDetails"
    IN SHARE ROW EXCLUSIVE MODE;

    -- 8. Generar ID de factura
    SELECT COALESCE(MAX("BillID"), 0) + 1
    INTO v_bill_id
    FROM "Bills";

    -- 9. Insertar factura
    INSERT INTO "Bills" (
        "BillID",
        "UserID",
        "Date",
        "Total"
    )
    VALUES (
        v_bill_id,
        v_user_id,
        CURRENT_DATE,
        v_total
    );

    -- 10. Insertar detalles de la factura
    INSERT INTO "BillDetails" (
        "DetailID",
        "BillID",
        "ProductID",
        "Quantity",
        "UnitPrice"
    )
    SELECT
        (
            SELECT COALESCE(MAX("DetailID"), 0)
            FROM "BillDetails"
        ) + ROW_NUMBER() OVER (
            ORDER BY p."ProductID"
        ),
        v_bill_id,
        p."ProductID",
        i.quantity,
        p."Price"
    FROM (
        SELECT
            product_id,
            SUM(quantity) AS quantity
        FROM purchase_items
        GROUP BY product_id
    ) i
    JOIN "Products" p
        ON p."ProductID" = i.product_id;

    -- 11. Descontar stock de los productos
    UPDATE "Products" p
    SET "Stock" = p."Stock" - i.quantity
    FROM (
        SELECT
            product_id,
            SUM(quantity) AS quantity
        FROM purchase_items
        GROUP BY product_id
    ) i
    WHERE p."ProductID" = i.product_id;

    -- 12. Mostrar confirmacion
    RAISE NOTICE
        'Compra exitosa. Factura: %, Total: %',
        v_bill_id,
        v_total;

END $$;

COMMIT;
