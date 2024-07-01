----1----

-- create table Customer (
-- 	id serial primary key,
-- 	first_name varchar(50),
-- 	last_name varchar(50) NOT NULL
-- );

-- create table Customer_profile (
-- 	id serial primary key,
-- 	isLoggedIn boolean DEFAULT false,
-- 	customer_id int,
-- 	foreign key (customer_id) references Customer(id)
-- );

-- insert into Customer (first_name, last_name) values 
-- 	('John', 'Doe'),
-- 	('Jerome', 'Lalu'),
-- 	('Lea', 'Rive');

-- insert into Customer_profile (customer_id, isLoggedIn) values
-- ((select id from Customer where first_name = 'John'), True),
-- ((select id from Customer where first_name = 'Jerome'), False);

-- select Customer.first_name 
-- from Customer
-- join Customer_profile on Customer.id = Customer_profile.customer_id
-- where Customer_profile.isLoggedIn = true

-- select Customer.first_name, Customer_profile.isLoggedIn
-- from Customer
-- left join Customer_profile on Customer.id = Customer_profile.id

-- select count(*) 
-- from Customer
-- left join Customer_profile on Customer.id = Customer_profile.customer_id
-- where Customer_profile.isLoggedIn = false or Customer_profile.isLoggedIn is NULL



----2----

-- create table Book (
-- 	book_id serial primary key,
-- 	title varchar(100) not null,
-- 	author varchar(50) not null
-- );

-- insert into Book (title, author) values
-- 	('Alice In Wonderland', 'Lewis Carroll'),
-- 	('Harry Potter', 'To kill a mockingbird, Harper LeeJ.K Rowling'),
-- 	('To kill a mockingbird', 'Harper Lee');

--  create table Student (
-- 	student_id serial primary key,
-- 	name varchar(100) not null unique,
-- 	age int
-- );

-- insert into Student (name, age) values 
-- ('John', 12),
-- ('Lera', 11),
-- ('Patrick', 10),
-- ('Bob', 14);

-- alter table Student
-- add constraint age_limit check (age <= 15);

-- create table Library (
-- 	book_fk_id int,
-- 	student_fk_id int,
-- 	borrowed_date date,
-- 	primary key (book_fk_id, student_fk_id),
-- 	foreign key (book_fk_id) references Book(book_id) on delete cascade on update cascade,
-- 	foreign key (student_fk_id) references Student(student_id) on delete cascade on update cascade
-- );

-- insert into Library (student_fk_id, book_fk_id, borrowed_date) values
-- ((select student_id from Student where name = 'John'), (select book_id from Book where title = 'Alice In Wonderland'), '2022-02-15');

-- insert into Library (student_fk_id, book_fk_id, borrowed_date) values
-- ((select student_id from Student where name = 'Bob'), (select book_id from Book where title = 'To kill a mockingbird'), '2021-03-03'),
-- ((select student_id from Student where name = 'Lera'), (select book_id from Book where title = 'Alice In Wonderland'), '2021-05-23'),
-- ((select student_id from Student where name = 'Bob'), (select book_id from Book where title = 'Harry Potter'), '2021-03-03');

-- select * from Library;

-- select Student.name, Book.title from Library
-- join Book on Library.book_fk_id = Book.book_id
-- join Student on Library.student_fk_id = Student.student_id;

-- select AVG(student.age) from Library
-- join Book on Library.book_fk_id = Book.book_id
-- join Student on Library.student_fk_id = Student.student_id
-- where Book.title = 'Alice in Wonderland';

-- delete from Student where name = 'John';
-- select * from Library