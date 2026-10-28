-- 1. Obtener todos los libros y sus autores, en caso de tenerlos
SELECT
    Books.Name AS Book,
    Authors.Name AS Author
FROM Books
LEFT JOIN Authors
    ON Books.Author = Authors.ID;

-- 2. Obtener todos los libros que no tienen autor
SELECT
    Books.ID,
    Books.Name
FROM Books
LEFT JOIN Authors
    ON Books.Author = Authors.ID
WHERE Authors.ID IS NULL;

-- 3. Obtener todos los autores que no tienen libros
SELECT
    Authors.ID,
    Authors.Name
FROM Authors
LEFT JOIN Books
    ON Authors.ID = Books.Author
WHERE Books.ID IS NULL;

-- 4. Obtener todos los libros que han sido rentados en algún momento
SELECT DISTINCT
    Books.ID,
    Books.Name
FROM Books
INNER JOIN Rents
    ON Books.ID = Rents.BookID;

-- 5. Obtener todos los libros que nunca han sido rentados
SELECT
    Books.ID,
    Books.Name
FROM Books
LEFT JOIN Rents
    ON Books.ID = Rents.BookID
WHERE Rents.ID IS NULL;

-- 6. Obtener todos los clientes que nunca han rentado un libro
SELECT
    Customers.ID,
    Customers.Name,
    Customers.Email
FROM Customers
LEFT JOIN Rents
    ON Customers.ID = Rents.CustomerID
WHERE Rents.ID IS NULL;

-- 7. Obtener todos los libros que han sido rentados
-- y están en estado "Overdue"
SELECT DISTINCT
    Books.ID,
    Books.Name
FROM Books
INNER JOIN Rents
    ON Books.ID = Rents.BookID
WHERE Rents.State = 'Overdue';