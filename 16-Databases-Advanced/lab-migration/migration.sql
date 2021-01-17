CREATE TABLE IF NOT EXISTS Persons (
    PersonID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255)
);

ALTER TABLE Persons 
ADD COLUMN Salary int;

ALTER TABLE Persons
DROP COLUMN LastName;