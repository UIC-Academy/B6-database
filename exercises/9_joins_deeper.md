# SQL JOINS deeper

### INNER JOIN (Fundamentals)

1. List each product name with its brand (assuming `brand_id → brand` mapping).
2. Show cart items with product names and user who owns the cart.
3. List all reviews with the product name and the reviewer's username.
4. Show all images with the associated product name.
5. Find all users who have reviewed at least one product, along with the review text.
6. List cart items with product price and total cost (`price * count`).
7. List each product with its available sizes.
8. Show products and their discount amounts (from `ProductDiscountM2M`).
9. List all product colors using the many-to-many color mapping.
10. List products that have images and reviews.

### LEFT JOIN (Optional Relationships)

1. List all users and any review they may have written (if any).
2. List all products and any image (show NULL if no image).
3. List all products and their discount (even if no discount exists).
4. Show each cart and the associated user's username.
5. Show each product and its sizes (if no size exists, show NULL).
6. List users and carts they own (some may not own any).
7. List all products and all their reviews (NULL if no review).
8. List all products with possible discounts and sizes.
9. List each cart item with possible related image of the product.
10. Show products with their reviews and their reviewers’ usernames (show product even if no review).

### RIGHT JOIN (Reverse Optional Relationships)

1. List all reviews and their users (some reviews may have lost user data).
2. List all images and the users who uploaded them (user may be deleted).
3. Show all cart items and the products they reference (may reference non-existent product).
4. List all product-color mappings, and the corresponding product names.
5. List all product-size mappings, and corresponding size names.
6. List all discount-product mappings and the product data.
7. Show all product reviews and include product name and user data.
8. Show all cart items and their carts (some orphaned cart items?).
9. Show all images and products they relate to (missing product shows NULL).
10. List all reviews and the full reviewer name (some with NULL).

### FULL OUTER JOIN (Complete Coverage)

1. List all products and all reviews (even if not matched).
2. List all users and all images (even if no user or image is missing).
3. List all carts and users (include unmatched).
4. Show all product-discount matches or standalone products/discounts.
5. List all products and their cart items (if any).
6. List all colors used and products using them (include orphan colors).
7. Show all sizes and products using them (if any).
8. List all reviews with user and product data, but include unmatched records.
9. List all cart items and related carts or products (fully matched or not).
10. List all image-product-user mappings (include all unmatched).

### CROSS JOIN (Combinations)

1. Get all possible combinations of users and products (for test data generation).
2. Show all possible color-size combinations.
3. List all combinations of users and discounts.
4. Generate a report of all possible cart-product pairs.
5. Show all possible product-review combinations (for mock matching).
6. Cross join products and sizes to simulate inventory planning.
7. Create a list of all user-product pairings (for recommender testing).
8. Combine all discounts and all products for testing future discount planning.
9. Cross join users and colors to simulate theme preferences.
10. Generate a full matrix of users, products, and sizes (three-table cross logic).