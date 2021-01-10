# Update statements
The UPDATE statement is used to modify the existing records in a table.

Syntax:
```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

Example:
```sql
UPDATE Customers
SET ContactName = 'Alfred Schmidt', City= 'Frankfurt'
WHERE CustomerID = 1;
```

Update multiple records:
```sql
UPDATE Customers
SET ContactName='Juan'
WHERE Country='Mexico';
```

> Note: Be careful when updating records. If you omit the WHERE clause, ALL records will be updated!
```sql
UPDATE Customers
SET ContactName='Juan';
```