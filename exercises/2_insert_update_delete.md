# INSERT, UPDATE, DELETE exercises

### **I. INSERT — 10 Exercises**

1. Insert a new customer named *Ali Karimov* living in the same city as *Mary Smith*.
2. Add a new film titled *"THE UNKNOWN ENGINEER"* with length 120 and rental rate 3.99.
3. Insert a new record into the `rental` table where *customer_id = 5* rents *inventory_id = 10* today.
4. Duplicate the address of *Store 1* for a new staff member named *John White*.
5. Insert 3 new actors: *Aisha Khan*, *Omar Malik*, and *Layla Noor*.
6. Add a new category called *“Machine Learning”* to the `category` table.
7. Add a new film in the *Machine Learning* category with rating `PG-13`.
8. Insert a new staff record that uses the same store as *Mike Hillyer* but a different email.
9. Insert a payment record for *customer_id = 8* for an amount of `5.99` with today’s date.
10. Insert a new language *“Uzbek”* into the `language` table.

### **II. UPDATE — 10 Exercises**

11. Update *Ali Karimov’s* email address in the `customer` table.
12. Increase all `rental_rate` values in the `film` table by `1.00` where the length > 150.
13. Change the *Machine Learning* category name to *“Artificial Intelligence”*.
14. Set `active = false` for customers who haven’t rented anything in the last 365 days.
15. Update all films longer than 180 minutes to have a `special_feature` of `'Deleted Scenes'`.
16. Reduce all payments greater than `10.00` by 10%.
17. Set the `last_update` column of all rows in `inventory` to the current timestamp.
18. Assign `store_id = 2` to all staff who currently belong to store 1.
19. Update the rating of all films containing “LOVE” in their title to `PG`.
20. Change *Omar Malik*’s last name to *Malyk*.

### **III. DELETE — 5 Exercises**

21. Delete all payments where amount = 0.00.
22. Remove all customers who have never made a payment.
23. Delete all films with a rental duration of 0 (if any).
24. Delete all addresses not linked to any staff, customer, or store.
25. Delete the *Artificial Intelligence* category (after unlinking all films from it).
