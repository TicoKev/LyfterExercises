
-- 1 Recreate all tables from the previous exercise

CREATE TABLE users(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  full_name VARCHAR(100) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  registration_date DATE NOT NULL
);


CREATE TABLE products(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  code CHAR(12) UNIQUE NOT NULL,
  name VARCHAR(30) NOT NULL,
  price REAL NOT NULL,
  entry_date DATE NOT NULL,
  brand VARCHAR(20) NOT NULL,
  stock_available SMALLINT NOT NULL
);


CREATE TABLE invoices(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  invoice_number INT UNIQUE NOT NULL,
  purchase_date DATE NOT NULL,
  total_amount INT NOT NULL
);


CREATE TABLE products_per_invoice(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  product_id INT REFERENCES products(id) NOT NULL,
  invoice_id INT REFERENCES invoices(id) NOT NULL,
  quantity INT NOT NULL,
  total_amount INT NOT NULL
);


CREATE TABLE shooping_cart(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  buyer_email VARCHAR(100) NOT NULL
);


CREATE TABLE shopping_cart_products(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  shopping_cart_id INT REFERENCES shooping_cart(id) NOT NULL,
  product_id INT REFERENCES products(id) NOT NULL
);


CREATE TABLE reviews(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  product_code CHAR(12) NOT NULL,
  comment TEXT,
  rating SMALLINT NOT NULL,
  date DATE NOT NULL
);


CREATE TABLE payment_method(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  method_type VARCHAR(25) NOT NULL,
  bank_name VARCHAR(30) NOT NULL
);

-- SQLITE Limitations
-- 1. Autogenerating IDs
--     To autogenerate IDs, we use the AUTOINCREMENT keyword, which starts at 1 and increases by 1 for each new 
--     row. However, the column must be declared as INTEGER, not INT.

-- 2. Date data type in SQLite
--     The DATE data type does not exist in SQLite, but SQLite is flexible and allows us to store dates as 
--     strings.

-- 2. ALTER command to modify the invoices table

ALTER TABLE invoices
  ADD buyer_phone_number VARCHAR(11) DEFAULT '00000000000' NOT NULL 


ALTER TABLE invoices
  ADD employee_code CHAR(6) DEFAULT 'ABC123' NOT NULL 


-- 3. SELECT Exercises

-- 1. Get all stored products
SELECT *
  FROM products;

-- 2. Get all products with a price greater than 50,000
SELECT *
  FROM products
  WHERE price > 50000;

-- 3. Get all purchases of the same product by ID
SELECT *
  FROM products_per_invoice
  WHERE product_id = 2;

-- 4.Get all purchases grouped by product, showing the total purchased across all purchases
SELECT product_id, SUM(total_amount) AS total_spent
  FROM products_per_invoice
  GROUP BY product_id
  ORDER by total_spent;

-- 5.Get all invoices made by the same buyer
SELECT invoice_number, purchase_date, total_amount
  FROM invoices
  WHERE buyer_phone_number = '+7875556331';

-- 6. Get all invoices ordered by total amount in descending order
SELECT *
  FROM invoices
  ORDER by total_amount DESC

-- 7.Get a single invoice by invoice number
SELECT *
  FROM invoices
  WHERE invoice_number = 2002