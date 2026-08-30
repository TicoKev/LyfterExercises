CREATE TABLE orders(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INT REFERENCES customers(id) NOT NULL,
  delivery_time DATETIME NOT NULL
);


CREATE TABLE customers(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(50) NOT NULL,
  customer_phone_number VARCHAR(20) NOT NULL
);


CREATE TABLE items(
  id INTEGER  PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(30) NOT NULL,
  price REAL NOT NULL DEFAULT 0
);


CREATE TABLE orders_items(
  order_id INT REFERENCES orders(id) NOT NUll,
  item_id INT REFERENCES items(id) NOT NULL,
  quantity INT NOT NULL,
  special_request TEXT DEFAULT 'NONE',
  PRIMARY KEY(order_id, item_id)
);


CREATE TABLE addresses(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  address_name VARCHAR(20) NOT NULL,
  customer_id INT REFERENCES customers(id) NOT NUll
);


-- Justification for the Orders Exercise

-- The way I approached this normalization process was by carefully analyzing the original table and identifying the main entities.
--Orders, Customers, and Items. Once the core tables were clear, I considered how they interact with each other.
--The most challenging part was deciding where to place the quantity attribute. At first, I thought it might belong in the Orders 
--table, but that would only represent the total quantity of items in an order, not the specific amount of each product. To resolve this, 
--I created a cross table orders_items that references both Orders and Items. This structure allows us to record how many units of each 
-- product were ordered, along with any special requests tied to that item.