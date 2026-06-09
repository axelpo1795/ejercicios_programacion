-- Productos
INSERT INTO Products (Code, Name, Price, Entry_Date, Brand, Stock_Available)
VALUES
(1, 'Laptop Lenovo', 650000, '2026-01-15', 'Lenovo', 10),
(2, 'Mouse Logitech', 15000, '2026-01-20', 'Logitech', 50),
(3, 'Monitor Samsung', 120000, '2026-02-01', 'Samsung', 15),
(4, 'Teclado Mecánico', 55000, '2026-02-10', 'Redragon', 20),
(5, 'SSD 1TB', 70000, '2026-03-05', 'Kingston', 30);

-- Facturas
INSERT INTO Invoices (Invoice_Number, Purchase_Date, Buyer_email, Total_Amount)
VALUES
(1001, '2026-05-01', 'juan@email.com', 680000),
(1002, '2026-05-03', 'maria@email.com', 190000),
(1003, '2026-05-05', 'juan@email.com', 85000),
(1004, '2026-05-07', 'carlos@email.com', 135000);

-- Ventas (detalle de facturas)
INSERT INTO Sales (Id_Sale, Invoice_Number, Product_Code, Quantity, Total_Amount)
VALUES
(1, 1001, 1, 1, 650000),
(2, 1001, 2, 2, 30000),

(3, 1002, 3, 1, 120000),
(4, 1002, 2, 2, 30000),
(5, 1002, 4, 1, 40000),

(6, 1003, 5, 1, 70000),
(7, 1003, 2, 1, 15000),

(8, 1004, 4, 2, 110000),
(9, 1004, 2, 1, 15000),
(10, 1004, 5, 1, 10000);

-- Carritos
INSERT INTO Shopping_Cart (Id_Cart, Buyer_email)
VALUES
(1, 'juan@email.com'),
(2, 'maria@email.com'),
(3, 'carlos@email.com');

-- Contenido de carritos
INSERT INTO Cart_Content (Id_Cart, Product_Code, Quantity)
VALUES
(1, 1, 1),
(1, 2, 2),
(2, 3, 1),
(2, 4, 1),
(3, 5, 2);