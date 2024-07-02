----1----

-- select name from language;


-- select film.title as title,
-- film.description as description,
-- language.name as language from film
-- join language on film.language_id = film.language_id;

-- select film.title as title,
-- film.description as description,
-- language.name as language from language
-- left join film on language.language_id = film.language_id; 

-- create table new_film (
-- 	id serial primary key,
-- 	name varchar(100)
-- );

-- insert into new_film (name) values
-- ('Gone with the wind'),
-- ('Lighthouse'),
-- ('Quiz Lady'),
-- ('Fill the void');

-- create table customer_review (
-- 	review_id serial primary key,
-- 	film_ad int references new_film(id) on delete cascade,
-- 	language_id int references language(language_id),
-- 	title varchar(100),
-- 	score int check (score between 1 and 10),
-- 	review_text text,
-- 	last_update DATE
-- );

-- alter table customer_review rename column film_ad to film_id;

-- insert into customer_review (film_id, language_id, title, score, review_text, last_update) values
-- (1, 1, 'it is a classic of cinematograph', 10, 'great movie to watch during holidays', '2024-07-02'),
-- (3, 1, 'nice for fun evening with friends', 6, 'comedy with a great cast', '2024-07-02');

-- delete from new_film where id = 3;
-- select * from customer_review  ---- review deleted too----


--2--

-- update film set language_id = 1 where id in (1, 2, 3);
-- select * from language;
-- select * from film where language_id = 1;
-- update film set language_id = (select language_id from language where name = 'Mandarin') 
-- where title in ('Chamber Italian' , 'Airport Pollock');
-- select * from film where language_id = 4;

--in customer we have the next foreign keys: store_id, adress_id; 

-- select * from customer_review; --easy--

-- select count(*) as not_return from rental
-- where return_date is NULL;

-- select film.title as title,
-- film.rental_rate as rate from rental
-- join inventory on rental.inventory_id = inventory.inventory_id
-- join film on inventory.film_id = film.film_id
-- where rental.return_date is NULL
-- order by rental_rate ASC
-- limit 30;

-- select title, description from film where description ilike '%The film is about a sumo wrestler%';

-- select title, rental_duration, rating from film where rating = 'R'and rental_duration <= 1;

-- 3 and 4 - didnt solve





