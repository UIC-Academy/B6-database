# The World of Databases

### What is a Database?

A database is a structured collection of data that can be easily accessed, managed, and updated.

### Why Do We Need Databases?

- **E-commerce:** Users, Products, Orders
- **Banking:** Accounts, Transactions
- **Social Media:** Users, Posts, Messages

##### ❗ Problem without Databases:

- What happens when 1,000 users try to save data at the same time?
- What if we need to find all users who bought a certain product?

**Databases solve this** with:

- **Concurrency control**
- **Security** and **access roles**
- **Querying languages** like SQL


### What is a DBMS?

**DBMS (Database Management System)** = software that helps us **interact with the database**.

Popular DBMSs:

- PostgreSQL
- MySQL
- SQLite
- Oracle
- MongoDB (NoSQL)

##### What does a DBMS do?

- Stores and retrieves data
- Handles security and users
- Backs up data
- Handles large amounts of data and multiple users

**PostgreSQL** is the DBMS we’ll use — it’s open-source, powerful, and widely respected.


### What is SQL?

**SQL = Structured Query Language**

SQL is the *language* we use to communicate with the DBMS.

### 🔠 SQL Categories:

- **DDL** – Data Definition Language (`CREATE TABLE`, `DROP TABLE`)
- **DML** – Data Manipulation Language (`INSERT`, `UPDATE`, `DELETE`)
- **DQL** – Data Query Language (`SELECT`)
- **DCL** – Data Control Language (`GRANT`, `REVOKE`)

### Why PostgreSQL?

PostgreSQL (or Postgres):

- Open-source, free to use
- Very strict with SQL standards
- Supports:
    - JSON fields
    - Indexes
    - Advanced queries
    - ACID compliance (Atomicity, Consistency, Isolation, Durability)


### Activity: Design a Student Database on Paper

Give students 10 minutes to design a basic database:

- Tables: Students(id, fullname, age, level, is_blocked), Courses(id, name, credit, professor), Enrollments
- What fields would each table have?
- What should be the primary key?

**Discussion**: How would we represent:

- A student enrolled in many courses?
- A course taken by many students?

## 📘 Homework

Database menga nima uchun kerak? Men ma’lumotlarimni fayllarda ham boshqara olamanku!