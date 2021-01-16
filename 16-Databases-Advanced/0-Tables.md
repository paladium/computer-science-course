# Tables & Databases

The CREATE DATABASE statement is used to create a new SQL database:
```sql
CREATE DATABASE databasename;
```

The CREATE TABLE statement is used to create a new table in a database.

Syntax:
```sql
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    column3 datatype,
   ....
);
```

Example:
```sql
CREATE TABLE Persons (
    PersonID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255)
);
```

## Drop tables & databases

The DROP DATABASE statement is used to drop an existing SQL database:
```sql
DROP DATABASE databasename;
```

The DROP TABLE statement is used to drop an existing table in a database.

Syntax:
```sql
DROP TABLE table_name;
```

Example:
```sql
DROP TABLE Shippers;
```

Delete all data, not deleting the table itself:
```sql
TRUNCATE TABLE table_name;
```

## Change table
The ALTER TABLE statement is used to add, delete, or modify columns in an existing table.

The ALTER TABLE statement is also used to add and drop various constraints on an existing table.

Syntax:
```sql
ALTER TABLE table_name
ADD column_name datatype;
```

Example:
```sql
ALTER TABLE Customers
ADD Email varchar(255);
```

Drop column:
```sql
ALTER TABLE table_name
DROP COLUMN column_name;
```

Drop column example:
```sql
ALTER TABLE Customers
DROP COLUMN Email;
```

Alter/Modify column:
```sql
ALTER TABLE table_name
ALTER COLUMN column_name datatype;
```

Alter/Modify column example:
```sql
ALTER TABLE Customers
ALTER COLUMN Email varchar(500);
```