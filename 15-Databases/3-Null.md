# Null value
A field with a NULL value is a field with no value.

If a field in a table is optional, it is possible to insert a new record or update a record without adding a value to this field. Then, the field will be saved with a NULL value.

Syntax:
```sql
SELECT column_names
FROM table_name
WHERE column_name IS NULL;
```

Not NULL:
```sql
SELECT column_names
FROM table_name
WHERE column_name IS NOT NULL;
```

Example - select all customers where Address is empty:
```sql
SELECT CustomerName, ContactName, Address
FROM Customers
WHERE Address IS NULL;
```

Example - select all customers where address is not empty:
```sql
SELECT CustomerName, ContactName, Address
FROM Customers
WHERE Address IS NOT NULL;
```