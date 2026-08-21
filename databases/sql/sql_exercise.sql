
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
  product_id REFERENCES products(id) NOT NUll,
  comment TEXT,
  rating SMALLINT NOT NULL,
  date DATE NOT NULL
);


CREATE TABLE payment_method(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  method_type VARCHAR(25) NOT NULL,
  bank_name VARCHAR(30) NOT NULL,
  invoice_id INT REFERENCES invoices(id) NOT NULL
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


-- Commands to add items to the tables

INSERT INTO users (full_name, email, registration_date)
  VALUES 
    ('John Smith', 'john.smith@example.com', '2026-08-01'),
    ('Emily Johnson', 'emily.johnson@example.com', '2026-08-05'),
    ('Michael Brown', 'michael.brown@example.com', '2026-08-10');

INSERT INTO products (code, name, price, entry_date, brand, stock_available)
  VALUES
    ('PRD1001', 'Gaming Laptop', 1200.50, '2026-08-01', 'Asus', 10),
    ('PRD1002', 'Wireless Mouse', 25.99, '2026-08-02', 'Logitech', 50),
    ('PRD1003', 'Mechanical Keyboard', 75.00, '2026-08-03', 'Corsair', 30),
    ('PRD1004', '4K OLED TV', 5200.00, '2026-08-04', 'Samsung', 5),
    ('PRD1005', 'Luxury Smartwatch', 6500.00, '2026-08-05', 'Apple', 8),
    ('PRD1006', 'Professional Camera', 7200.00, '2026-08-06', 'Canon', 4);

INSERT INTO invoices (invoice_number, purchase_date, total_amount, buyer_phone_number, employee_code)
  VALUES
    (2001, '2026-08-10', 8644.46, '+7872361219', 'EMP001'),
    (2002, '2026-08-12', 16727.48, '+9613214731', 'EMP002'),
    (2003, '2026-08-15', 20925.50, '+7875556331', 'EMP001'),
    (2004, '2026-08-18', 7200.00, '+50688887777', 'EMP003'),
    (2005, '2026-08-19', 7450.50, '+50699996666', 'EMP002');

INSERT INTO shopping_cart (buyer_email)
  VALUES
    ('john.smith@example.com'),
    ('emily.johnson@example.com');

INSERT INTO shopping_cart_products (shopping_cart_id, product_id)
  VALUES
  (1, 3),   
  (1, 6),   
  (2, 4);

INSERT INTO reviews (product_code, comment, rating, date)
  VALUES
    ('PRD001', 'Excellent performance, very fast.', 5, '2026-08-12'),
    ('PRD002', 'Comfortable but the battery does not last long.', 3, '2026-08-14'),
    ('PRD003', 'Keyboard with good sound and quality.', 4, '2026-08-16');

INSERT INTO payment_method (method_type, bank_name)
  VALUES
    ('Credit Card', 'Bank of America'),
    ('PayPal', ''),
    ('Wire Transfer', 'Chase Bank');

INSERT INTO products_per_invoice (product_id, invoice_id, quantity, total_amount)
  VALUES
    (1, 1, 1, 1200.50),
    (2, 1, 1, 25.99),
    (3, 1, 2, 150.00),
    (2, 1, 3, 77.97),
    (6, 1, 1, 7200.00),
    (4, 2, 1, 5200.00),
    (4, 2, 2, 10400.00),
    (1, 2, 1, 1200.50),
    (3, 2, 1, 75.00),
    (2, 2, 2, 51.98),
    (5, 3, 1, 6500.00),
    (5, 3, 2, 13000.00),
    (1, 3, 1, 1200.50),
    (3, 3, 3, 225.00),
    (6, 4, 1, 7200.00),
    (1, 5, 1, 1200.50),
    (6, 5, 1, 6250.00);

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