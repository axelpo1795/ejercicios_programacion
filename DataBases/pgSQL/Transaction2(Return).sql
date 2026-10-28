
BEGIN;

SET LOCAL search_path TO "BillsSchema";

DO $$
DECLARE
    v_bill_id INTEGER := 1;
    v_status VARCHAR(20);
    v_product RECORD;
BEGIN

    -- 1. Verificar que la factura existe
    -- y bloquearla durante la devolucion
    SELECT "Status"
    INTO v_status
    FROM "Bills"
    WHERE "BillID" = v_bill_id
    FOR UPDATE;

    IF NOT FOUND THEN
        RAISE EXCEPTION
            'La factura % no existe', v_bill_id;
    END IF;

    -- 2. Verificar que no haya sido retornada
    IF v_status = 'Retornada' THEN
        RAISE EXCEPTION
            'La factura % ya fue retornada',
            v_bill_id;
    END IF;

    -- 3. Verificar que tenga productos registrados
    IF NOT EXISTS (
        SELECT 1
        FROM "BillDetails"
        WHERE "BillID" = v_bill_id
    ) THEN
        RAISE EXCEPTION
            'La factura % no contiene productos',
            v_bill_id;
    END IF;

    -- 4. Aumentar stock de los productos
    FOR v_product IN
        SELECT
            "ProductID",
            SUM("Quantity") AS quantity
        FROM "BillDetails"
        WHERE "BillID" = v_bill_id
        GROUP BY "ProductID"
    LOOP

        UPDATE "Products"
        SET "Stock" = "Stock" + v_product.quantity
        WHERE "ProductID" = v_product."ProductID";

        IF NOT FOUND THEN
            RAISE EXCEPTION
                'El producto % no existe',
                v_product."ProductID";
        END IF;

    END LOOP;

    -- 5. Marcar la factura como retornada
    UPDATE "Bills"
    SET "Status" = 'Retornada'
    WHERE "BillID" = v_bill_id;

    -- 6. Mostrar confirmacion
    RAISE NOTICE
        'Factura % retornada correctamente',
        v_bill_id;

END $$;

COMMIT;
