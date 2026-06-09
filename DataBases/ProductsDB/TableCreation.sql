-- SQLite
CREATE TABLE Products (
    Code INTEGER PRIMARY KEY,
    Name varchar(100) NOT NULL,
    Price FLOAT NOT NULL,
    Entry_Date DATE NOT NULL,
    Brand varchar(50) NOT NULL,
    Stock_Available INTEGER NOT NULL
);

CREATE TABLE Invoices (
    Invoice_Number INTEGER PRIMARY KEY,
    Purchase_Date DATE NOT NULL,
    Buyer_email varchar(100) NOT NULL,
    Total_Amount FLOAT NOT NULL
);

CREATE TABLE Shopping_Cart (
    Id_Cart INTEGER PRIMARY KEY,
    Buyer_email varchar(100) NOT NULL
);

CREATE TABLE Sales (
    Id_Sale INTEGER PRIMARY KEY,
    Invoice_Number INTEGER NOT NULL,
    Product_Code INTEGER NOT NULL,
    Quantity INTEGER NOT NULL,
    Total_Amount FLOAT NOT NULL,
    FOREIGN KEY (Invoice_Number) REFERENCES Invoices(Invoice_Number),
    FOREIGN KEY (Code) REFERENCES Products(Code)
);

CREATE TABLE Cart_Content (
    Id_Cart INTEGER NOT NULL,
    Product_Code INTEGER NOT NULL,
    Quantity INTEGER NOT NULL,
    PRIMARY KEY (Id_Cart),
    FOREIGN KEY (Id_Cart) REFERENCES Shopping_Cart(Id_Cart),
    FOREIGN KEY (Product_Code) REFERENCES Products(Code)
);