# Delete
The DELETE statement is used to delete existing records in a table.

Syntax:
```sql
DELETE FROM table_name WHERE condition;
```

Example:
```sql
DELETE FROM Customers WHERE CustomerName='Alfreds Futterkiste';
```

Delete all records:
```sql
DELETE FROM table_name;
```

Example (delete all records from Customers table):
```sql
DELETE FROM Customers;
```