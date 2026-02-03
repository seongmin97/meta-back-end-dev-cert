## Intro
- SQL subsets
  - Data define language
  - Data manipulation language
  - Data query language
  - Data control language
- SQL syntax intro
  - create
  - insert
- Types of key
  - Primary key
  - Candidate key: Any attribute that can uniquely identify a record (e.g., staff ID and contact numbers).
  - Composite key: Formed by combining two or more attributes to create a unique identifier.
  - Foreign key

## CRUD operation
- Numeric data type
  - integer: TINYINT (max 255), INT
  - decimal

```sql
# lab exercies
CREATE DATABASE cm_devices;
USE cm_devices

CREATE TABLE devices( deviceID int, deviceName varchar(50), price decimal);
show tables;

INSERT INTO devices (deviceID, deviceName, price) 
VALUES (1, 'iPhone XR 1', 1500.50);

CREATE TABLE customers(username CHAR(9), fullName VARCHAR(100), email VARCHAR(255)); 

CREATE TABLE feedback(
    feedbackID CHAR(8), 
    feedbackType VARCHAR(100), 
    comment TEXT(500)
);

```

- String data type
  - CHAR: fix length
  - VARCHAR: variable lenght, length can be changed. Data only occupied as much length as it is.
  - TEXT:
- Date data type
- Default value
  - NOT NULL

```sql
CREATE TABLE Address (id int NOT NULL,  street VARCHAR(255), postcode VARCHAR(10) DEFAULT "HA97DE", town VARCHAR(30) DEFAULT "Harrow");
```
- ALTER TABLE statement
  - ADD column
  - DROP column
  - MODIFY column
- INSERT statement
- INSERT INTO SELECT statement
  - `INSERT INTO country(countryName) SELECT country FROM players`
- UPDATE data
```sql
UPDATE student_tbl
SET college_address = 'xxx building', student_phone = '1234567890'
WHERE id = 3;
```
- DELETE
  - Remove all the records in a table: DELETE FROM customers;
  - `TRUNCATE TABLE staff` clears all rows from the table while keeping its schema. It is faster than DELETE FROM staff and resets auto-increment counters, but it cannot be rolled back in most cases.


## SQL operators

## Database design
