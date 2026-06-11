SELECT * FROM Products;

SELECT *
FROM Products
WHERE Price > 50000;

SELECT
    Sales.Invoice_Number,
    Products.Name,
    Sales.Quantity,
    Sales.Total_Amount
FROM Sales
INNER JOIN Products
    ON Sales.Product_Code = Products.Code
WHERE Products.Code = 1;

SELECT
    Products.Name,
    SUM(Sales.Quantity) AS Total_Units,
    SUM(Sales.Total_Amount) AS Total_Sales
FROM Sales
INNER JOIN Products
    ON Sales.Product_Code = Products.Code
GROUP BY Products.Code, Products.Name;

SELECT *
FROM Invoices
WHERE Buyer_email = 'juan@email.com';

SELECT *
FROM Invoices
ORDER BY Total_Amount DESC;

SELECT *
FROM Invoices
WHERE Invoice_Number = 1002;