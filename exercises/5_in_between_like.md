# IN, BETWEEN, LIKE, ILIKE

### **Table: film**

1. Select all films where `rating` IN ('PG', 'PG-13').
2. Select all films where `rental_rate` IN (0.99, 2.99, 4.99).
3. Select films whose `length` BETWEEN 90 AND 120 minutes.
4. Select films with `replacement_cost` BETWEEN 15 AND 20.
5. Select films whose `title` LIKE 'A%'.
6. Select films whose `title` LIKE '%Love%'.
7. Select films whose `title` LIKE '%Man%'.
8. Select films whose `title` LIKE '_A%'.
9. Select films whose `description` ILIKE '%adventure%'.
10. Select films whose `description` ILIKE '%police%' AND `rating` = 'R'.

---

### **Table: customer**

11. Select customers whose `first_name` LIKE 'A%'.
12. Select customers whose `last_name` LIKE '%son'.
13. Select customers whose `first_name` ILIKE 'm%'.
14. Select customers whose `email` LIKE '%@sakilacustomer.org'.
15. Select customers whose `create_date` BETWEEN '2006-01-01' AND '2006-06-30'.
16. Select customers whose `store_id` IN (1, 2).
17. Select customers whose `last_name` ILIKE '%LL%'.
18. Select customers whose `first_name` LIKE 'J%' AND `active` = 1.
19. Select customers whose `email` ILIKE '%example%'.
20. Select customers whose `first_name` IN ('MARY', 'PATRICIA', 'LINDA').

---

### **Table: payment**

21. Select payments whose `amount` BETWEEN 5 AND 8.
22. Select payments whose `payment_date` BETWEEN '2005-07-01' AND '2005-07-15'.
23. Select payments whose `amount` IN (0.99, 2.99, 4.99).
24. Select payments where `amount` NOT IN (0.99, 2.99).
25. Select payments whose `payment_date::text` LIKE '2005-07%'.
26. Select payments whose `amount` BETWEEN 8 AND 10 AND `staff_id` = 1.
27. Select payments whose `payment_date` BETWEEN '2005-06-01' AND '2005-06-30' AND `amount` > 5.
28. Select payments where `customer_id` IN (1, 2, 3, 4, 5).
29. Select payments whose `amount` BETWEEN 1 AND 3 OR `amount` BETWEEN 8 AND 10.
30. Select payments whose `payment_date::text` ILIKE '%2005-07-3%'.

