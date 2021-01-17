# Database migrations
Let's create a new file with our schema:
```sql
CREATE TABLE IF NOT EXISTS Persons (
    PersonID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255)
);
```
> Note: it is important to create table only if does not exist, otherwise we will get an exception.

To run migrations on first run, we should do the following:
```python
with open('schema.sql') as f:
    cursor.execute(f.read(), multi=True)
```