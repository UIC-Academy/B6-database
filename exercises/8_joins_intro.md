# SQL JOINS 

## Introduction

### Level 1: Basic INNER JOINs (Single Join)

1. **List all film titles and their language names.**
    
    *(Join `film` and `language`)*
    
2. **Show the first and last names of all actors who acted in the film "ACADEMY DINOSAUR".**
    
    *(Join `actor`, `film_actor`, `film`)*
    
3. **Display all customer names and their email addresses.**
    
    *(Join `customer` with no other table — warm-up)*
    
4. **List customer full names and the names of the stores they registered at.**
    
    *(Join `customer` and `store`)*
    
5. **Show all films and their categories.**
    
    *(Join `film`, `film_category`, `category`)*
    
6. **List staff members and their respective store address.**
    
    *(Join `staff`, `address`)*
    
7. **Get the titles of all films rented by customer “MARY SMITH”.**
    
    *(Join `customer`, `rental`, `inventory`, `film`)*

### Level 2: Two-table Joins with Filters

1. **List the names of all customers who rented at least one film.**
    
    *(Join `customer` and `rental` with DISTINCT)*
    
2. **Show all films that are in the 'Comedy' category.**
    
    *(Join `film_category`, `category`, `film` with filter on category name)*
    
3. **List all payments along with the customer names who made them.**
    
    *(Join `payment` and `customer`)*
    
4. **Get the titles and rental rates of all films longer than 120 minutes.**
    
    *(Join `film` only — no join needed — easy confidence builder)*
    
5. **List the staff who processed each rental transaction.**
    
    *(Join `rental` and `staff`)*
    
6. **Display all customers and the cities they live in.**
    
    *(Join `customer`, `address`, `city`)*
    

### 🔹 Level 3: Multi-table Joins

1. **List all customers and the films they have rented, with the film title and rental date.**
    
    *(Join `customer`, `rental`, `inventory`, `film`)*
    
2. **Show film titles, actor names, and categories.**
    
    *(Join `film`, `film_actor`, `actor`, `film_category`, `category`)*
    
3. **Find all rentals and include customer name, staff name, film title, and rental date.**
    
    *(Join `rental`, `customer`, `staff`, `inventory`, `film`)*
    
4. **Display a list of customers, their email, and the store city they are associated with.**
    
    *(Join `customer`, `store`, `address`, `city`)*
    
5. **List the top 10 most rented films with the number of times each was rented.**
    
    *(Join `rental`, `inventory`, `film` + `GROUP BY` + `COUNT`)*


## INNER JOIN

### Basic Level

1. List all films with their language names.
2. Show all actors with their film titles.
3. Display customer names with their corresponding rental dates.
4. Find all staff members and the addresses where they work.
5. List all payments with customer names who made them.

### Intermediate Level

1. Show film titles and their categories.
2. Display actor names with the number of films they've appeared in.
3. Find customers who rented films from a specific store (store_id = 1).
4. List all films rented in May 2005 with customer names.
5. Show staff members who processed payments over $5.00.

### Advanced Level

1. Find films rented more than 10 times with their rental counts.
2. Display customers who rented films from multiple categories.
3. List actors who appeared in films from at least 3 different categories.
4. Find films that were never rented but are in inventory.
5. Show customers who rented the same film more than once.

### Complex Queries

1. Find the most popular film category based on rental count.
2. Display customers who rented all films from a particular actor.
3. List films that were rented on consecutive days by the same customer.
4. Find actors who only appeared in R-rated films.
5. Show customers who rented from both stores (store_id 1 and 2).

### Business Scenarios

1. Identify the top 5 customers by total spending.
2. Find the most profitable film category.
3. List staff members with their total processed payment amounts.
4. Show films that are consistently rented every month.
5. Find customers who haven't rented in the last 6 months.

### Challenging Problems

1. Display customers who rented films from all categories.
2. Find actors who have worked together in multiple films.
3. List films with above-average rental rates but below-average replacement costs.
4. Show customers whose rental frequency increased month-over-month.
5. Find the longest gap between rentals for each customer.