# GROUP BY Lesson Plan

## Part 1: Introduction

### What is GROUP BY?
GROUP BY is like organizing items into buckets based on a common characteristic, then calculating statistics for each bucket.

**Real-world analogy:** Imagine you have a box of colored marbles. GROUP BY is like separating them by color, then counting how many marbles of each color you have.

### Basic Syntax
```sql
SELECT column_name, AGGREGATE_FUNCTION(column_name)
FROM table_name
GROUP BY column_name;
```

## Part 2: Hands-On Examples

### Example 1: Simple COUNT - "How many films are in each rating category?"

```sql
SELECT rating, COUNT(*) as number_of_films
FROM film
GROUP BY rating;
```

**Explain:** 
- We're grouping all films by their rating (G, PG, PG-13, R, NC-17)
- COUNT(*) counts how many films are in each group
- Result shows each rating and its count

**Expected output:** 5 rows showing each rating and its film count

---

### Example 2: Using SUM - "What's the total payment amount per customer?"

```sql
SELECT customer_id, SUM(amount) as total_spent
FROM payment
GROUP BY customer_id
ORDER BY total_spent DESC
LIMIT 10;
```

**Explain:**
- Groups all payments by customer_id
- SUM(amount) adds up all payment amounts for each customer
- ORDER BY shows biggest spenders first
- LIMIT 10 shows only top 10 customers

---

### Example 3: Multiple Columns - "How many films per category and rating?"

```sql
SELECT c.name as category, f.rating, COUNT(*) as film_count
FROM film f
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
GROUP BY c.name, f.rating
ORDER BY c.name, f.rating;
```

**Explain:**
- Groups by BOTH category AND rating
- Creates separate groups for each unique combination
- Example: "Action + PG-13" is different from "Action + R"

---

### Example 4: Using AVG - "Average rental duration per rating"

```sql
SELECT rating, 
       AVG(rental_duration) as avg_rental_days,
       ROUND(AVG(rental_rate), 2) as avg_price
FROM film
GROUP BY rating
ORDER BY avg_price DESC;
```

**Explain:**
- AVG() calculates the average value
- ROUND() makes the decimal easier to read
- Shows which ratings have longer rental periods and higher prices

---

### Example 5: HAVING clause - "Which customers spent more than $100?"

```sql
SELECT customer_id, SUM(amount) as total_spent
FROM payment
GROUP BY customer_id
HAVING SUM(amount) > 100
ORDER BY total_spent DESC;
```

**Explain:**
- HAVING is like WHERE, but for grouped data
- WHERE filters rows BEFORE grouping
- HAVING filters groups AFTER aggregation
- Use HAVING when you need to filter based on aggregate functions

---

## Part 3: Common Mistakes to Avoid

### Mistake 1: Selecting non-grouped columns
```sql
-- WRONG ❌
SELECT customer_id, first_name, SUM(amount)
FROM payment
JOIN customer USING(customer_id)
GROUP BY customer_id;

-- CORRECT ✓
SELECT customer_id, first_name, SUM(amount)
FROM payment
JOIN customer USING(customer_id)
GROUP BY customer_id, first_name;
```

**Rule:** Every column in SELECT must either be:
1. In the GROUP BY clause, OR
2. Inside an aggregate function (COUNT, SUM, AVG, etc.)

### Mistake 2: Using WHERE with aggregates
```sql
-- WRONG ❌
SELECT customer_id, SUM(amount)
FROM payment
WHERE SUM(amount) > 100  -- Can't use aggregate in WHERE
GROUP BY customer_id;

-- CORRECT ✓
SELECT customer_id, SUM(amount)
FROM payment
GROUP BY customer_id
HAVING SUM(amount) > 100;
```

---

## Part 4: Practice Exercises (10 minutes)

Have students try these queries:

1. **Easy:** Count how many customers are in each city
2. **Medium:** Find the total number of rentals per store
3. **Challenge:** Which actor has appeared in the most films?

### Solutions:

```sql
-- 1. Customers per city
SELECT city, COUNT(*) as customer_count
FROM customer
JOIN address USING(address_id)
JOIN city USING(city_id)
GROUP BY city
ORDER BY customer_count DESC;

-- 2. Rentals per store
SELECT store_id, COUNT(*) as rental_count
FROM rental
JOIN staff USING(staff_id)
GROUP BY store_id;

-- 3. Most prolific actor
SELECT a.first_name, a.last_name, COUNT(*) as film_count
FROM actor a
JOIN film_actor fa USING(actor_id)
GROUP BY a.actor_id, a.first_name, a.last_name
ORDER BY film_count DESC
LIMIT 1;
```

---

# 10 Real-World Analogies for GROUP BY Intuition

## Exercise 1: The Fruit Basket
**Scenario:** You have a basket with 50 fruits: apples, oranges, bananas, and grapes.

**Task:** Organize them by fruit type and count each.

**SQL Equivalent:**
```sql
SELECT fruit_type, COUNT(*) as quantity
FROM fruit_basket
GROUP BY fruit_type;
```

**Result Visualization:**
- Apples bucket: 15 fruits
- Oranges bucket: 12 fruits
- Bananas bucket: 18 fruits
- Grapes bucket: 5 fruits

---

## Exercise 2: The Classroom Grade Book
**Scenario:** You're a teacher with student grades. You want to know the average grade for each subject.

**Think:** Put all Math tests in one pile, all English tests in another pile, then calculate the average for each pile.

**SQL Equivalent:**
```sql
SELECT subject, AVG(grade) as average_grade
FROM student_grades
GROUP BY subject;
```

**Mental Picture:**
- Math pile → Average: 85
- English pile → Average: 78
- Science pile → Average: 92

---

## Exercise 3: The Parking Lot
**Scenario:** A parking lot has cars of different colors. Count how many cars of each color are parked.

**Think:** Walk through the lot, create a group for each color you see, count them.

**SQL Equivalent:**
```sql
SELECT color, COUNT(*) as car_count
FROM parked_cars
GROUP BY color;
```

**Student Activity:** Ask students: "If you had to organize this manually, how would you do it?" (They'll naturally describe grouping!)

---

## Exercise 4: The Restaurant Orders
**Scenario:** A restaurant wants to know total revenue from each dish type (appetizers, main courses, desserts).

**Think:** Separate all appetizer orders, add up their prices. Do the same for main courses and desserts.

**SQL Equivalent:**
```sql
SELECT dish_type, SUM(price) as total_revenue
FROM orders
GROUP BY dish_type;
```

**Real Numbers:**
- Appetizers: $450 total
- Main Courses: $2,300 total
- Desserts: $680 total

---

## Exercise 5: The Library Books
**Scenario:** A library wants to find the oldest book in each genre.

**Think:** Create a shelf for Fiction, another for Non-Fiction, another for Biography, then find the oldest book on each shelf.

**SQL Equivalent:**
```sql
SELECT genre, MIN(publication_year) as oldest_book_year
FROM library_books
GROUP BY genre;
```

**Visualization:**
- Fiction shelf → Oldest: 1847
- Non-Fiction shelf → Oldest: 1923
- Biography shelf → Oldest: 1901

---

## Exercise 6: The Sports Tournament
**Scenario:** You have basketball game scores. Find the highest score achieved by each team.

**Think:** Create a folder for each team, put all their game scores in their folder, find the highest score in each folder.

**SQL Equivalent:**
```sql
SELECT team_name, MAX(points_scored) as highest_score
FROM game_scores
GROUP BY team_name;
```

**Example:**
- Lakers folder → Highest: 128 points
- Warriors folder → Highest: 135 points
- Celtics folder → Highest: 118 points

---

## Exercise 7: The Online Store
**Scenario:** An e-commerce site wants to know how many orders came from each country.

**Think:** Sort shipping labels by country, count how many labels in each country's stack.

**SQL Equivalent:**
```sql
SELECT country, COUNT(*) as order_count
FROM orders
GROUP BY country;
```

**Interactive Question:** "If you were sorting physical mail by country, what would you do?" (Students describe grouping naturally!)

---

## Exercise 8: The Movie Theater
**Scenario:** A cinema wants the average ticket price for each movie rating (G, PG, PG-13, R).

**Think:** Create 4 boxes labeled with each rating, put ticket prices in appropriate boxes, calculate average for each box.

**SQL Equivalent:**
```sql
SELECT rating, AVG(ticket_price) as avg_price
FROM movie_tickets
GROUP BY rating;
```

**Results:**
- G-rated box → Average: $8.50
- PG-rated box → Average: $9.00
- PG-13 box → Average: $10.50
- R-rated box → Average: $11.00

---

## Exercise 9: The Weather Station
**Scenario:** You have daily temperature readings for different cities. Find the average temperature for each city.

**Think:** Create a notebook page for each city, write all that city's temperatures on its page, calculate the average.

**SQL Equivalent:**
```sql
SELECT city, AVG(temperature) as avg_temp
FROM weather_readings
GROUP BY city;
```

**Visualization:**
- New York page → Average: 65°F
- Los Angeles page → Average: 72°F
- Chicago page → Average: 58°F

---

## Exercise 10: The Hospital Emergency Room
**Scenario:** Hospital wants to know the total number of patients by severity level (Critical, Serious, Stable).

**Think:** Use colored wristbands - Red for Critical, Yellow for Serious, Green for Stable. Count each color.

**SQL Equivalent:**
```sql
SELECT severity_level, COUNT(*) as patient_count
FROM er_patients
GROUP BY severity_level;
```

**Triage Visualization:**
- Red (Critical) → 8 patients
- Yellow (Serious) → 23 patients
- Green (Stable) → 45 patients

---

# Now Let's Apply to Sakila Database

## Sakila Practice with Real-World Thinking

### Practice 1: The DVD Store Inventory
**Real-world:** "Organize all DVDs by their rating and count them - like organizing physical DVDs on different shelves"

```sql
SELECT rating, COUNT(*) as film_count
FROM film
GROUP BY rating
ORDER BY film_count DESC;
```

### Practice 2: Customer Spending Patterns
**Real-world:** "Each customer has a spending folder. Add up all their payments to see who spends the most"

```sql
SELECT c.first_name, c.last_name, SUM(p.amount) as total_spent
FROM customer c
JOIN payment p USING(customer_id)
GROUP BY c.customer_id, c.first_name, c.last_name
ORDER BY total_spent DESC
LIMIT 10;
```

---

# Introducing HAVING: Filtering the Buckets

## The Key Concept

**Real-world analogy:** 
Imagine you've organized fruits into buckets by type AND counted them. Now you say: "**Show me only the buckets that have MORE than 10 fruits**"

- WHERE filters INDIVIDUAL fruits BEFORE putting them in buckets
- HAVING filters ENTIRE BUCKETS AFTER counting

## Visual Example

```
BEFORE GROUPING (WHERE works here):
[apple, apple, orange, orange, apple, banana, orange, apple]
WHERE color = 'red' → Removes non-red fruits first

AFTER GROUPING (HAVING works here):
Apples bucket: 15 fruits
Oranges bucket: 8 fruits
Bananas bucket: 3 fruits

HAVING COUNT(*) > 10 → Shows only Apples bucket
```

---

# WHERE vs HAVING: The Critical Difference

## Example 1: The Restaurant Orders (Clear Distinction)

### Scenario: Find customers who ordered desserts AND spent more than $50 total

```sql
-- Step 1: WHERE filters individual orders BEFORE grouping
-- Step 2: GROUP BY creates customer buckets
-- Step 3: HAVING filters the buckets AFTER summing

SELECT customer_id, SUM(amount) as total_spent
FROM orders
WHERE dish_type = 'dessert'  -- Filter individual orders first
GROUP BY customer_id
HAVING SUM(amount) > 50;     -- Filter the grouped totals
```

**Think of it as:**
1. WHERE: "Only look at dessert orders" (filters rows)
2. GROUP BY: "Make a pile for each customer"
3. HAVING: "Show only piles that total more than $50" (filters groups)

---

## Example 2: WHERE Cannot Use Aggregates

```sql
-- ❌ WRONG - This will give an ERROR
SELECT customer_id, SUM(amount)
FROM payment
WHERE SUM(amount) > 100  -- ERROR! Can't use aggregate in WHERE
GROUP BY customer_id;

-- ✓ CORRECT - Use HAVING for aggregate conditions
SELECT customer_id, SUM(amount)
FROM payment
GROUP BY customer_id
HAVING SUM(amount) > 100;
```

**Why?** WHERE works on individual rows BEFORE they're grouped. At that point, SUM() doesn't exist yet!

---

# Sakila Database: WHERE vs HAVING Examples

## Example 1: Active Customers Who Are Big Spenders

**Question:** "Find active customers who have spent more than $150 total"

```sql
SELECT c.customer_id, 
       c.first_name, 
       c.last_name, 
       SUM(p.amount) as total_spent
FROM customer c
JOIN payment p USING(customer_id)
WHERE c.active = 1                    -- WHERE: Filter before grouping
GROUP BY c.customer_id, c.first_name, c.last_name
HAVING SUM(p.amount) > 150            -- HAVING: Filter after summing
ORDER BY total_spent DESC;
```

**Breakdown:**
- WHERE active = 1: "Only look at active customers" (filters individual customer records)
- GROUP BY: "Create a spending summary for each customer"
- HAVING SUM > 150: "Show only customers whose total exceeds $150" (filters the summaries)

---

## Example 2: Recent Rentals from Popular Films

**Question:** "Which films rented in 2005 have been rented more than 30 times?"

```sql
SELECT f.title, COUNT(*) as rental_count
FROM film f
JOIN inventory i USING(film_id)
JOIN rental r USING(inventory_id)
WHERE EXTRACT(YEAR FROM r.rental_date) = 2005  -- WHERE: Filter rentals by year
GROUP BY f.film_id, f.title
HAVING COUNT(*) > 30                           -- HAVING: Filter by rental count
ORDER BY rental_count DESC;
```

**The Logic:**
1. WHERE filters rental records to only 2005 (before grouping)
2. GROUP BY creates a rental count for each film
3. HAVING shows only films with 30+ rentals (after counting)

---

## Example 3: High-Value Customers in Specific Cities

**Question:** "Find customers in cities starting with 'L' who spent more than $120"

```sql
SELECT ci.city,
       c.first_name,
       c.last_name,
       SUM(p.amount) as total_spent
FROM customer c
JOIN address a USING(address_id)
JOIN city ci USING(city_id)
JOIN payment p USING(customer_id)
WHERE ci.city LIKE 'L%'               -- WHERE: Filter cities before grouping
GROUP BY ci.city, c.customer_id, c.first_name, c.last_name
HAVING SUM(p.amount) > 120            -- HAVING: Filter totals after grouping
ORDER BY total_spent DESC;
```

---

## Example 4: PG-13 Films with Long Average Rental Duration

**Question:** "Which PG-13 film categories have an average rental duration over 5 days?"

```sql
SELECT cat.name as category,
       COUNT(*) as film_count,
       ROUND(AVG(f.rental_duration), 2) as avg_rental_days
FROM film f
JOIN film_category fc USING(film_id)
JOIN category cat USING(category_id)
WHERE f.rating = 'PG-13'                      -- WHERE: Only PG-13 films
GROUP BY cat.category_id, cat.name
HAVING AVG(f.rental_duration) > 5             -- HAVING: Categories with avg > 5
ORDER BY avg_rental_days DESC;
```

---

# The Decision Tree: WHERE or HAVING?

Ask students these questions:

**Question 1:** "Am I filtering based on a column value in the original table?"
- YES → Use WHERE
- Example: `WHERE rating = 'PG-13'`, `WHERE active = 1`

**Question 2:** "Am I filtering based on a calculation across grouped rows?"
- YES → Use HAVING
- Example: `HAVING SUM(amount) > 100`, `HAVING COUNT(*) > 50`

**Question 3:** "Can I calculate this BEFORE grouping the data?"
- YES → Use WHERE
- NO → Use HAVING

---

# Practice Exercises: WHERE vs HAVING

Have students identify whether to use WHERE or HAVING:

1. Show customers who live in 'Canada' and spent more than $100
2. Find films longer than 120 minutes that have been rented more than 25 times
3. List actors who appeared in R-rated films at least 10 times
4. Show categories with more than 60 films that have an average replacement cost over $20

### Solutions:

```sql
-- 1. WHERE for country, HAVING for spending
SELECT c.customer_id, c.first_name, c.last_name, SUM(p.amount) as total
FROM customer c
JOIN address a USING(address_id)
JOIN city ci USING(city_id)
JOIN country co USING(country_id)
JOIN payment p USING(customer_id)
WHERE co.country = 'Canada'
GROUP BY c.customer_id, c.first_name, c.last_name
HAVING SUM(p.amount) > 100;

-- 2. WHERE for film length, HAVING for rental count
SELECT f.title, f.length, COUNT(*) as rental_count
FROM film f
JOIN inventory i USING(film_id)
JOIN rental r USING(inventory_id)
WHERE f.length > 120
GROUP BY f.film_id, f.title, f.length
HAVING COUNT(*) > 25;

-- 3. WHERE for rating, HAVING for appearance count
SELECT a.first_name, a.last_name, COUNT(*) as film_count
FROM actor a
JOIN film_actor fa USING(actor_id)
JOIN film f USING(film_id)
WHERE f.rating = 'R'
GROUP BY a.actor_id, a.first_name, a.last_name
HAVING COUNT(*) >= 10;

-- 4. HAVING for both conditions (both are aggregates)
SELECT c.name, 
       COUNT(*) as film_count,
       ROUND(AVG(f.replacement_cost), 2) as avg_cost
FROM category c
JOIN film_category fc USING(category_id)
JOIN film f USING(film_id)
GROUP BY c.category_id, c.name
HAVING COUNT(*) > 60 AND AVG(f.replacement_cost) > 20;
```
