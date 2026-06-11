ALTER TABLE Invoices
    ADD Client_Number varchar(8) NOT NULL;

ALTER TABLE Invoices
    ADD Employee_Id INTEGER;

ALTER TABLE Invoices
    RENAME Client_Number TO Client_Phone_Number;