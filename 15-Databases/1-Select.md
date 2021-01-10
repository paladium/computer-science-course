# SQL syntax intro

A database most often contains one or more tables. Each table is identified by a name (e.g. "Customers" or "Orders"). Tables contain records (rows) with data.

If we have the table, named Customers, with the following data (https://www.w3schools.com/sql/trysql.asp?filename=trysql_op_in):

|CustomerID|CustomerName|Address|Country|
|-|-|-|-|
|1|Alfreds Futterkiste|Obere Str. 57|Germany|
|2|Ana Trujillo Emparedados y helados|Avda. de la Constitución 2222|Mexico|
|3|Antonio Moreno Taquería|Mataderos 2312|Mexico|
|4|Around the Horn|120 Hanover Sq.|UK|
|5|Berglunds snabbköp|Berguvsvägen 8|Sweden|

We have 5 records and 4 columns: CustomerID, CustomerName, Address, Country.

We can use the following statement to extract all the data:
```sql
SELECT * FROM Customers;
```
> Note: You can use both uppercase and lowercase commands, like select or from, but the table name should match the original table name.

## Select
We can use the SELECT command to select the data we need.

The general syntax is the following:
```sql
SELECT column1, column2, ...
FROM table_name;
```
So we can specify which columns we want in our result.

If we only need to select CustomerID and their Country:
```sql
SELECT CustomerID, Country FROM Customers;
```

## Select where
We can now specify conditions based on which we will select our data:
```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```
Let's say we want to select all the Customers where the country is Mexico:
```sql
SELECT * FROM Customers
WHERE Country='Mexico';
```
We can also use it to find a single record based on unique id:
```sql
SELECT * FROM Customers
WHERE CustomerID=1;
```
Possible operators:
|Operator|Description|Example|
|-|-|-|
|=|Equal|
|>|Greater than|
|<|Less than|
|>=|Greater than or equal|
|<=|Less than or equal|
|<>|Not equal. Note: In some versions of SQL this operator may be written as !=|
|BETWEEN|Between a certain range|SELECT * FROM Products WHERE Price BETWEEN 50 AND 60;|
|LIKE|Search for a pattern|SELECT * FROM Customers WHERE City LIKE 's%';|
|IN|To specify multiple possible values for a column|SELECT * FROM Customers WHERE City IN ('Paris','London');|

## And or

The WHERE clause can be combined with AND, OR, and NOT operators.

The AND and OR operators are used to filter records based on more than one condition:

- The AND operator displays a record if all the conditions separated by AND are TRUE.
- The OR operator displays a record if any of the conditions separated by OR is TRUE.
- The NOT operator displays a record if the condition(s) is NOT TRUE.

### And syntax
```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition1 AND condition2 AND condition3 ...;
```
Example:
```sql
SELECT * FROM Customers
WHERE Country='Germany' AND City='Berlin';
```

### Or syntax
```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition1 OR condition2 OR condition3 ...;
```

Example:
```sql
SELECT * FROM Customers
WHERE City='Berlin' OR City='München';
```

### Not syntax
```sql
SELECT column1, column2, ...
FROM table_name
WHERE NOT condition;
```
Example:
```sql
SELECT * FROM Customers
WHERE NOT Country='Germany';
```

### Combining AND, OR and NOT
You can also combine the AND, OR and NOT operators.

The following SQL statement selects all fields from "Customers" where country is "Germany" AND city must be "Berlin" OR "München" (use parenthesis to form complex expressions):
```sql
SELECT * FROM Customers
WHERE Country='Germany' AND (City='Berlin' OR City='München');
```


## Order-by
The ORDER BY keyword is used to sort the result-set in ascending or descending order.

The ORDER BY keyword sorts the records in ascending order by default. To sort the records in descending order, use the DESC keyword.

```sql
SELECT column1, column2, ...
FROM table_name
ORDER BY column1, column2, ... ASC|DESC;
```

Example:
```sql
SELECT * FROM Customers
ORDER BY Country;
```

The following SQL statement selects all customers from the "Customers" table, sorted DESCENDING by the "Country" column:
```sql
SELECT * FROM Customers
ORDER BY Country DESC;
```

The following SQL statement selects all customers from the "Customers" table, sorted by the "Country" and the "CustomerName" column. This means that it orders by Country, but if some rows have the same Country, it orders them by CustomerName:
```sql
SELECT * FROM Customers
ORDER BY Country, CustomerName;
```

> Note: ORDER BY should come after WHERE statement.