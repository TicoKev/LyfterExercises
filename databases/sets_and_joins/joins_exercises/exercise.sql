CREATE TABLE books(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(100) NOT NULL,
  author_id INT REFERENCES authors(id)
);

CREATE TABLE authors(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(45) NOT NUll
);

CREATE TABLE customers(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(45) NOT NULL,
  email VARCHAR(50) NOT NUll
);

CREATE TABLE rents(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  book_id INT REFERENCES books(id),
  customer_id INT REFERENCES customers(id),
  state VARCHAR(15) NOT NULL
);


--Inserts

INSERT INTO books (name, author_id)
VALUES
  ('Don Quijote', 1),
  ('La Divina Comedia', 2),
  ('Vagabond 1-3', 3),
  ('Dragon Ball 1', 4),
  ('The Book of the 5 Rings', NULL);


INSERT INTO authors (name)
VALUES
  ('Miguel de Cervantes'),
  ('Dante Alighieri'),
  ('Takehiko Inoue'),
  ('Akira Toriyama'),
  ('Walt Disney');


INSERT INTO customers (name, email)
VALUES
  ('John Doe', 'j.doe@email.com'),
  ('Jane Doe', 'jane@doe.com'),
  ('Luke Skywalker', 'darth.son@email.com');


INSERT INTO rents (bookid, customerid, state)
VALUES
  (1, 2, 'Returned'),
  (2, 2, 'Returned'),
  (1, 1, 'On time'),
  (3, 1, 'On time'),
  (2, 2, 'Overdue');


--Exercise queries

--1.
SELECT books.name AS book_name, authors.name AS author_name
  FROM books
  JOIN authors ON books.author_id = authors.id
  WHERE books.author_id IS NOT NULL

-- 2.
SELECT books.name
  FROM books
  WHERE books.author_id IS NULL

--3.
SELECT authors.name
  FROM authors
  LEFT JOIN books ON authors.id = books.author_id
  WHERE books.id IS NULL;

--4.
SELECT DISTINCT books.id, books.name
  FROM books
  JOIN rents ON books.id = rents.book_id
  WHERE state IN ('Returned', 'On Time', 'Overdue');

--5.
SELECT books.id, books.name
  FROM books
  LEFT JOIN rents ON books.id = rents.book_id
  WHERE rents.book_id IS NULL

--6.
SELECT customers.id, customers.name
  FROM customers
  LEFT JOIN rents ON customers.id = rents.customer_id
  WHERE rents.customer_id IS NULL

--7.
SELECT books.id, books.name
  FROM books
  LEFT JOIN rents ON books.id = rents.book_id
  WHERE rents.state = 'Overdue'