# Filtering and Aggregate Functions Exercises

### **IV. WHERE, ORDER BY, LIMIT, AND/OR/NOT — 15 Exercises**

26. Retrieve all films with rental_rate > 2.99 **and** length < 90.
27. Find all customers whose first name starts with `'M'` **or** `'A'`.
28. List all films that are **not** rated `'R'`.
29. Find all customers who live in *Texas* **and** have active = true.
30. Retrieve the top 10 most recently added films using `ORDER BY film_id DESC LIMIT 10`.
31. List 5 actors whose first names end with `'a'` using `LIMIT`.
32. Find all staff whose email contains `'@sakilacustomer.org'`.
33. Display all payments greater than `5.00` but less than `10.00`.
34. List the 10 shortest films that have `'ACTION'` in their title.
35. Find all inactive customers (`active = false`).
36. Retrieve all rentals where the return date is still NULL.
37. Display 10 addresses from countries **not** equal to `'United States'`.
38. Find all films released after 2005 **and** rated `'PG'` or `'G'`.
39. List all customers who have rented a film containing `'DOG'` in the title.
40. Retrieve the 5 most expensive films (highest rental_rate) sorted descending.

---

### **V. Aggregate Functions — 10 Exercises**

*(No GROUP BY or HAVING; only aggregates applied to the full result set.)*
41. Count total number of films in the database.
42. Find the average film length.
43. Calculate the minimum and maximum rental rate.
44. Count total number of customers.
45. Find the sum of all payments ever made.
46. Calculate the average payment amount.
47. Find the total number of rentals.
48. Find the earliest and latest rental dates.
49. Compute the average replacement cost of all films with `rating = 'PG-13'`.
50. Count how many films have length greater than 120.
