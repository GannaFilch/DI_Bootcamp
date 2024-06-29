-- select * from customer;

-- select concat(first_name, ' ', last_name) as full_name
-- from customer;

-- select distinct create_date from customer;

-- select * from customer order by first_name DESC;

-- select film_id, title, description, release_year, rental_rate from film order by rental_rate ASC;


-- select address.address, address.phone
-- from customer
-- join address on customer.address_id = address.address_id
-- where address.district = 'Texas';

-- select * from film where film_id in (15, 150);

-- select film_id, title, description, length, rental_rate from film where title = 'gone with the wind';

-- select film_id, title, description, length, rental_rate from film where title like 'go%';

-- select title, rental_rate from film order by rental_rate limit 10;

-- select title, rental_rate from film order by rental_rate limit 10 offset 10;

-- select customer.first_name, customer.last_name, payment.amount, payment.payment_date
-- from customer
-- join payment on customer.customer_id = payment.customer_id 
-- order by customer.customer_id

-- select title from film
-- left join inventory on film.film_id = inventory.film_id
-- where inventory.film_id is NULL

-- select city.city, country.country from city
-- right join country on city.country_id = country.country_id






