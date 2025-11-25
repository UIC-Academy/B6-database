# GROUP BY & HAVING

* `SELECT`, `WHERE`, `GROUP BY`, `HAVING`,
* aggregates: `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`.

### **Table: payment**

1. Count total number of payments.
2. Find total amount paid (sum of all amounts).
3. Calculate average payment amount.
4. Find the smallest and largest payment amounts.
5. Count how many payments each customer made.
6. Total amount paid by each customer.
7. Average payment amount per customer.
8. Customers who made more than 10 payments.
9. Customers whose total payments exceed 150.
10. Customers whose average payment exceeds 5.
11. Count of payments per staff member.
12. Total amount collected by each staff.
13. Staff who collected more than 1000 in total.
14. Average payment per staff.
15. Number of payments made on each date.

---

### **Table: rental**

16. Count total rentals.
17. Find the earliest and latest rental dates.
18. Count how many rentals each customer made.
19. Customers with more than 20 rentals.
20. Average number of rentals per day (using `GROUP BY rental_date::date`).
21. Count how many times each staff processed a rental.
22. Staff with more than 100 rentals handled.
23. Count of rentals per return_date (group by return_date).
24. Days where more than 50 rentals occurred.
25. Average rental_id per staff (nonsensical mathematically, but forces use of aggregate).

---

### **Table: customer**

26. Count total customers.
27. Count customers by `active` status.
28. Count customers by `store_id`.
29. Stores having more than 300 customers.
30. Average customer ID per store (training grouping only).
31. Count customers by `create_date` (group by date).
32. Count how many customers were added per day.
33. Days where more than 5 customers were added.

---

### **Table: film**

34. Count how many films exist per rating.
35. Ratings that have more than 200 films.
36. Average rental rate per rating.
37. Average length per rating.
38. Ratings with average rental rate above 3.0.
39. Count how many films have the same replacement cost.
40. Replacement cost values that appear in more than 10 films.

