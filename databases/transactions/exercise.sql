CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    full_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    brand VARCHAR(35) NOT NULL,
    stock INT DEFAULT 0
);

CREATE TABLE bills (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    purchase_date DATE DEFAULT CURRENT_DATE,
    total DECIMAL(10,2) NOT NULL
);


CREATE TABLE bills_products (
    bill_id INT REFERENCES bills(id),
    product_id INT REFERENCES products(id),
    quantity INT NOT NULL,
    subtotal DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (bill_id, product_id)
);


-- status column added to bills table

ALTER TABLE bills ADD COLUMN status TEXT;

-- Purchase transaction

DO $$
DECLARE 
    buyer_user_id INT := 1;
    v_bill_id INT;
BEGIN
    IF NOT EXISTS(SELECT 1 FROM users WHERE id = buyer_user_id) THEN
        RAISE EXCEPTION 'The user does not exist.';
    END IF;

    INSERT INTO bills(user_id, purchase_date, total)
    VALUES(buyer_user_id, CURRENT_DATE, 0)
    RETURNING id INTO v_bill_id;

    IF (SELECT stock FROM products WHERE id = 1) < 1 THEN
        RAISE EXCEPTION 'Not enough stock for Laptop';
    END IF;
    IF (SELECT stock FROM products WHERE id = 2) < 2 THEN
        RAISE EXCEPTION 'Not enough stock for Headphones';
    END IF;

    INSERT INTO bills_products (bill_id, product_id, quantity, subtotal)
    VALUES (v_bill_id, 1, 1, (SELECT price FROM products WHERE id = 1));

    INSERT INTO bills_products (bill_id, product_id, quantity, subtotal)
    VALUES (v_bill_id, 2, 2, (SELECT price*2 FROM products WHERE id = 2));

    UPDATE products SET stock = stock - 1 WHERE id = 1;
    UPDATE products SET stock = stock - 2 WHERE id = 2;

    UPDATE bills
    SET total = (SELECT SUM(subtotal) FROM bills_products WHERE bill_id = v_bill_id)
    WHERE id = v_bill_id;

    RAISE NOTICE 'Purchase successful. Bill ID: %', v_bill_id;
END;
$$;


-- Return product transaction

DO $$
DECLARE
    v_bill_id INT := 1;
BEGIN
    IF NOT EXISTS (SELECT 1 FROM bills WHERE id = v_bill_id) THEN
        RAISE EXCEPTION 'The bill does not exist.';
    END IF;

    UPDATE products p
    SET stock = stock + bp.quantity
    FROM bills_products bp
    WHERE bp.bill_id = v_bill_id
      AND bp.product_id = p.id;

    UPDATE bills
    SET total = 0,
        purchase_date = CURRENT_DATE,
        status = 'Returned'
    WHERE id = v_bill_id;

    RAISE NOTICE 'Return processed successfully. Bill ID: %', v_bill_id;
END;
$$;
