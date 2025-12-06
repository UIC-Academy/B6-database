# NULLS, CONSTRAINTS and KEYS

### **NULL Handling**

1. Select all customers whose `email` IS NULL.
2. Select all customers whose `email` IS NOT NULL.
3. Count how many films have a `release_year` IS NULL.
4. Select all rentals where `return_date` IS NULL (i.e., not returned).
5. Count rentals where `return_date` IS NOT NULL.
6. Select all staff records where `picture` IS NULL.
7. Select all payments where `amount` IS NULL (should return none — tests understanding).
8. Find all addresses where `address2` IS NULL.
9. Count how many addresses have `address2` filled (IS NOT NULL).
10. Select all films where `special_features` IS NULL (to confirm if column allows NULL).

---

### **Constraints & Keys Inspection**

11. View structure of `customer` table using `\d customer`; identify the **primary key**.
12. View structure of `film` table; list all **NOT NULL** columns.
13. View structure of `rental` table; identify which columns form the **primary key**.
14. Attempt to insert a duplicate value into a primary key column (should fail).
15. Attempt to insert a record missing a **NOT NULL** column (should fail).
16. Identify which columns in `customer` table have **DEFAULT** values.
17. View which column(s) in `rental` table are **foreign keys** (read only, not use them).
18. Check if `payment_id` column in `payment` table is marked as `PRIMARY KEY`.
19. Find which columns in `film` table have **CHECK** or **DEFAULT** constraints (e.g., rental_rate, rating).
20. Inspect `store` table; identify its **primary key** and any **unique** constraints.



---


NOT NULL - Ensures that a column cannot have a NULL value
UNIQUE - Ensures that all values in a column are different
PRIMARY KEY - A combination of a NOT NULL and UNIQUE. Uniquely identifies each row in a table
FOREIGN KEY - Prevents actions that would destroy links between tables
CHECK - Ensures that the values in a column satisfies a specific condition
DEFAULT - Sets a default value for a column if no value is specified
CREATE INDEX - Used to create and retrieve data from the database very quickly
