-- Ex1: Retrieve all data from the film table.
select * from film;

-- Ex2: Retrieve the first_name and last_name from the customer table.
select first_name, last_name from customer;

-- Ex3: Retrieve all unique rating values from the film table.
select distinct rating from film;

-- Ex4: Retrieve all films with a rental_rate greater than 4.00.
explain analyze
select * from film
where rental_rate > 4.00;

-- Ex5: Retrieve the actors whose first_name is exactly 'PENELOPE'.
select * from actor
where first_name = 'PENELOPE';

-- Ex6: Insert a new actor with first_name 'LUCY' and last_name 'VAN PELT'.
insert into actor(first_name, last_name)
values ('LUCY', 'VAN PELT');

select * from actor
order by actor_id DESC
limit 2;

-- Ex7: Retrieve the film with the title exactly 'ACADEMY DINOSAUR'.
select * from film
where title='ACADEMY DINOSAUR';

-- Ex9: Retrieve all films with a replacement_cost less than 10.00.
select * from film
where replacement_cost < 10.00;

-- Ex 16: Insert a new category with the name 'MYSTERY'.
insert into category(name)
values ('MYSTERY');

-- Ex 19: Retrieve all unique combinations of rating and rental_duration from the film table.
select distinct rating, rental_duration from film;

-- Ex22: Retrieve all films with a rating of 'G', 'PG', or 'PG-13'.
explain analyze
select * from film
where rating = 'G' or rating = 'PG' or rating = 'PG-13';

explain analyze
select * from film
where rating in ('G', 'PG', 'PG-13');

-- Ex25: Retrieve all films with a rental_rate between 1.00 and 3.00.
select * from film
where rental_rate >= 1.00 and rental_rate <= 3.00
order by rental_rate asc;

select * from film
where rental_rate between 1.00 and 3.00;

-- Ex27: Retrieve all films with a replacement_cost between 12.00 and 18.00.
select * from film
where replacement_cost between 12.00 and 18.00;

-- Ex31: Insert two new actors: ('BILL', 'MURRAY'), ('SIGOURNEY', 'WEAVER').
insert into actor(first_name, last_name)
values ('BILL', 'MURRAY'), ('SIGOURNEY', 'WEAVER');

select * from actor
order by actor_id DESC
limit 2;

-- Ex45: Retrieve customers with store_id 1 AND (active is 1 OR first_name is 'JENNIFER').
select * from customer
where active = 0 or first_name = 'JENNIFER' and store_id = 1;

-- Ex47: Retrieve films that are NOT rated 'G' AND NOT rated 'PG-13'.
select * from film
where rating <> 'G' and rating <> 'PG-13';

-- Ex52: Retrieve the titles of all films that have the special feature exactly 'Trailers'.
explain analyze
select title, special_features
from film
where 'Trailers' = any(special_features) and array_length(special_features, 1) = 1;

-- Ex58: Retrieve the titles of all films where the description is exactly 'A Epic Drama of a Feminist And a Mad Scientist who must Battle a Woman in A Jet Boat'.
select title from film
where description = 'A Epic Drama of a Feminist And a Mad Scientist who must Battle a Woman in A Jet Boat';

-- Ex59: Retrieve the customer IDs of all inactive customers whose email address is '[email address removed]'.
select customer_id from customer
where active=0 and email = '[email address removed]';

update customer
set active=0, email='[email address removed]'
where customer_id = 5;

-- Ex63: Retrieve the titles of all films released in 2006 that have a 'R' rating and a replacement cost greater than 20.00.
select title from film
where release_year = '2006' and rating = 'R' and replacement_cost > 20.00;