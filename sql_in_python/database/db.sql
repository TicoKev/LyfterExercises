--Task 1

-- Users script

SET search_path TO lyfter_car_rental;


CREATE TYPE acc_state AS ENUM ('active', 'suspended', 'closed');

CREATE TABLE users (
	id SERIAL PRIMARY KEy,
	name VARCHAR(50) NOT NULl,
	username VARCHAR(50) UNIQUE NOT NULl,
	email VARCHAR(100) UNIQUE NOT NULl,
	user_password VARCHAR(255) NOT NULl,
	date_of_birth DATE NOT NULl,
	account_state acc_state DEFAULT 'active' NOT NULL,
  is_delinquent BOOLEAN DEFAULT FALSE NOT NULL
);


INSERT INTO users (name, username, email, user_password, date_of_birth, account_state) VALUES ('Arabela Phelan', 'aphelan0', 'aphelan0@wordpress.org', 'jD3%XxtI?8..GH,', '1961-11-22', 'active');
INSERT INTO users (name, username, email, user_password, date_of_birth, account_state) VALUES ('Elenore Paxman', 'epaxman1', 'epaxman1@nsw.gov.au', 'nN4_a*..h%Rvva', '1989-12-31', 'active');
INSERT INTO users (name, username, email, user_password, date_of_birth, account_state) VALUES ('Duff Pettis', 'dpettis2', 'dpettis2@ycombinator.com', 'zU5*Bs1dF(FT#B.H', '1988-08-26', 'active');
INSERT INTO users (name, username, email, user_password, date_of_birth, account_state) VALUES ('Fair Brane', 'fbrane3', 'fbrane3@hexun.com', 'xF3$Rqoyjum', '1996-11-15', 'active');
INSERT INTO users (name, username, email, user_password, date_of_birth, account_state) VALUES ('Valerie Accomb', 'vaccomb4', 'vaccomb4@wikipedia.org', 'zU1$/Tj6zbc', '2005-08-24', 'active');
INSERT INTO users (name, username, email, user_password, date_of_birth, account_state) VALUES ('Drucie Rowdell', 'drowdell5', 'drowdell5@blinklist.com', 'cP9)KcOX%i', '1960-02-23', 'active');
INSERT INTO users (name, username, email, user_password, date_of_birth, account_state) VALUES ('Vita Leys', 'vleys6', 'vleys6@wikipedia.org', 'qZ5@Gs}37', '1998-02-10', 'suspended');
INSERT INTO users (name, username, email, user_password, date_of_birth, account_state) VALUES ('Claudianus Jewel', 'cjewel7', 'cjewel7@narod.ru', 'vW6{kI,8', '1989-12-10', 'suspended');
INSERT INTO users (name, username, email, user_password, date_of_birth, account_state) VALUES ('Dareen Fyers', 'dfyers8', 'dfyers8@posterous.com', 'tR7bpT?E?JjmS*a6X', '1978-04-01', 'suspended');
INSERT INTO users (name, username, email, user_password, date_of_birth, account_state) VALUES ('Sutton Grieger', 'sgrieger9', 'sgrieger9@list-manage.com', 'wW3)9EV`', '1989-12-18', 'closed');
INSERT INTO users (name, username, email, user_password, date_of_birth, account_state) VALUES ('Maximilianus Cunnah', 'mcunnaha', 'mcunnaha@uol.com.br', 'pE6(NcJ5,#X62U_', '1985-03-06', 'closed');
INSERT INTO users (name, username, email, user_password, date_of_birth, account_state) VALUES ('Ryon Tattersfield', 'rtattersfieldb', 'rtattersfieldb@netlog.com', 'aQ12v/IpM%H2b', '1988-05-01', 'suspended');
INSERT INTO users (name, username, email, user_password, date_of_birth, account_state) VALUES ('Abraham Franke', 'afrankec', 'afrankec@aboutads.info', 'mU6=~Oa.>l', '2008-04-25', 'active');
INSERT INTO users (name, username, email, user_password, date_of_birth, account_state) VALUES ('Odelia Condit', 'oconditd', 'oconditd@bbc.co.uk', 'mC9/<+iw4xW#9', '1972-09-23', 'active');
INSERT INTO users (name, username, email, user_password, date_of_birth, account_state) VALUES ('Sutherland Spillane', 'sspillanee', 'sspillanee@addthis.com', 'bS6+EWC<x>7W_O|', '1980-03-18', 'suspended');
INSERT INTO users (name, username, email, user_password, date_of_birth, account_state) VALUES ('Bram Stammirs', 'bstammirsf', 'bstammirsf@patch.com', 'jE9_uYZu$F0=J', '1979-02-08', 'active');
INSERT INTO users (name, username, email, user_password, date_of_birth, account_state) VALUES ('Abba Dicty', 'adictyg', 'adictyg@blogspot.com', 'pY3@@<?>J#T?O|<', '1984-05-11', 'active');
INSERT INTO users (name, username, email, user_password, date_of_birth, account_state) VALUES ('Jarad Tyas', 'jtyash', 'jtyash@ycombinator.com', 'nN2{tCY(=Z5a.94#', '1961-09-26', 'suspended');
INSERT INTO users (name, username, email, user_password, date_of_birth, account_state) VALUES ('Fonz Melrose', 'fmelrosei', 'fmelrosei@1688.com', 'uP3}4d>_TX..\\', '1977-09-25', 'suspended');
INSERT INTO users (name, username, email, user_password, date_of_birth, account_state) VALUES ('Rustie Tonkinson', 'rtonkinsonj', 'rtonkinsonj@behance.net', 'kI8|jeJ#Yp(b', '1974-01-02', 'active');
INSERT INTO users (name, username, email, user_password, date_of_birth, account_state) VALUES ('Dominick Pinching', 'dpinchingn', 'dpinchingn@foxnews.com', 'fE9/Fd<+w!?18r', '1977-12-13', 'suspended');
INSERT INTO users (name, username, email, user_password, date_of_birth, account_state) VALUES ('Theodor Petche', 'tpetcheo', 'tpetcheo@hugedomains.com', 'zT7@3yLAO}2G3', '1962-02-24', 'closed');
INSERT INTO users (name, username, email, user_password, date_of_birth, account_state) VALUES ('Codie Bignold', 'cbignoldp', 'cbignoldp@irs.gov', 'dX7"CJQ+c$_(', '2005-04-13', 'suspended');
INSERT INTO users (name, username, email, user_password, date_of_birth, account_state) VALUES ('Fianna Ochterlonie', 'fochterlonieq', 'fochterlonieq@tinypic.com', 'vY8/av$@a', '2006-02-25', 'suspended');
INSERT INTO users (name, username, email, user_password, date_of_birth, account_state) VALUES ('Shaylah Karlsen', 'skarlsenr', 'skarlsenr@etsy.com', 'lR4\\A_bng2', '1995-07-17', 'closed');
INSERT INTO users (name, username, email, user_password, date_of_birth, account_state) VALUES ('Penelope Nodin', 'pnodins', 'pnodins@soundcloud.com', 'jY6/78WOO.wGas#k!', '1980-02-07', 'suspended');
INSERT INTO users (name, username, email, user_password, date_of_birth, account_state) VALUES ('Leicester Vettore', 'lvettoret', 'lvettoret@rambler.ru', 'pI7#ng|DXYE{#O2', '1967-10-17', 'active');
INSERT INTO users (name, username, email, user_password, date_of_birth, account_state) VALUES ('Zola Bonny', 'zbonnyu', 'zbonnyu@facebook.com', 'eL6"hi<U#LZ~*7', '1986-09-26', 'active');
INSERT INTO users (name, username, email, user_password, date_of_birth, account_state) VALUES ('Jaquelyn Brinded', 'jbrindedv', 'jbrindedv@nps.gov', 'yZ0yuyaM0n', '1950-06-20', 'active');
INSERT INTO users (name, username, email, user_password, date_of_birth, account_state) VALUES ('Janey Darter', 'jdarterw', 'jdarterw@amazon.co.jp', 'rK3(<}0|q4DVFZ', '1956-08-22', 'suspended');
INSERT INTO users (name, username, email, user_password, date_of_birth, account_state) VALUES ('Lamont Poppleton', 'lpoppletonx', 'lpoppletonx@huffingtonpost.com', 'eJ8}X$sQB_aJV0|', '1995-11-08', 'active');
INSERT INTO users (name, username, email, user_password, date_of_birth, account_state) VALUES ('Creight Jennens', 'cjennensy', 'cjennensy@i2i.jp', 'sH5,TU)3|', '1976-09-21', 'active');
INSERT INTO users (name, username, email, user_password, date_of_birth, account_state) VALUES ('Velvet Dantesia', 'vdantesiaz', 'vdantesiaz@4shaactive.com', 'qX1~>RRbE', '1973-10-31', 'suspended');
INSERT INTO users (name, username, email, user_password, date_of_birth, account_state) VALUES ('Gregory Peckham', 'gpeckham10', 'gpeckham10@marketwatch.com', 'bA0)FpH2&Nh9o"', '1965-12-22', 'active');
INSERT INTO users (name, username, email, user_password, date_of_birth, account_state) VALUES ('Kelbee Boobier', 'kboobier11', 'kboobier11@europa.eu', 'fG9~BF9u$Co', '1997-10-23', 'suspended');
INSERT INTO users (name, username, email, user_password, date_of_birth, account_state) VALUES ('Kip Kennermann', 'kkennermann12', 'kkennermann12@walmart.com', 'kR4(9D"dq@', '1950-01-12', 'suspended');
INSERT INTO users (name, username, email, user_password, date_of_birth, account_state) VALUES ('Dillie Jeckells', 'djeckells13', 'djeckells13@dagondesign.com', 'gY7?eX)o~MX<', '2002-02-02', 'suspended');
INSERT INTO users (name, username, email, user_password, date_of_birth, account_state) VALUES ('Baldwin Gudgion', 'bgudgion14', 'bgudgion14@intel.com', 'uX2|$6ACs#"H2', '2004-08-07', 'active');
INSERT INTO users (name, username, email, user_password, date_of_birth, account_state) VALUES ('Jacinthe Livock', 'jlivock15', 'jlivock15@hugedomains.com', 'qJ1|fKCxF', '1959-07-19', 'closed');
INSERT INTO users (name, username, email, user_password, date_of_birth, account_state) VALUES ('Ingelbert Klimkov', 'iklimkov16', 'iklimkov16@google.cn', 'bI3{?`z,Ql.l9V|l', '1980-03-21', 'active');
INSERT INTO users (name, username, email, user_password, date_of_birth, account_state) VALUES ('Brock Wyllcock', 'bwyllcock17', 'bwyllcock17@msn.com', 'kV4*oHgwBC%IU9Q', '1972-11-08', 'active');
INSERT INTO users (name, username, email, user_password, date_of_birth, account_state) VALUES ('Austin Habble', 'ahabble18', 'ahabble18@miibeian.gov.cn', 'rX2%O@|ftQ<', '1979-08-02', 'closed');
INSERT INTO users (name, username, email, user_password, date_of_birth, account_state) VALUES ('Jerrie Boffin', 'jboffin19', 'jboffin19@forbes.com', 'qQ8@Z76y2', '1995-03-30', 'closed');
INSERT INTO users (name, username, email, user_password, date_of_birth, account_state) VALUES ('Richardo Speare', 'rspeare1a', 'rspeare1a@cnbc.com', 'iD1|M8yB*', '1950-11-25', 'active');
INSERT INTO users (name, username, email, user_password, date_of_birth, account_state) VALUES ('Carlita Tootal', 'ctootal1b', 'ctootal1b@linkedin.com', 'jR7,UY3qLbhGAS', '1994-08-10', 'active');
INSERT INTO users (name, username, email, user_password, date_of_birth, account_state) VALUES ('Kacie Gyrgorwicx', 'kgyrgorwicx1c', 'kgyrgorwicx1c@liveinternet.ru', 'pO0{_uW.W"ai}5)T', '1957-06-19', 'active');
INSERT INTO users (name, username, email, user_password, date_of_birth, account_state) VALUES ('Janella Ritchley', 'jritchley1d', 'jritchley1d@fotki.com', 'cW2=}jmXG<=*qEN', '1971-03-27', 'active');
INSERT INTO users (name, username, email, user_password, date_of_birth, account_state) VALUES ('Maribel Quintero', 'mquintero20', 'mquintero20@example.com', 'aB7!xYz#Qw', '1990-07-14', 'active');
INSERT INTO users (name, username, email, user_password, date_of_birth, account_state) VALUES ('Esteban Solano', 'esolano21', 'esolano21@example.com', 'pT9$LmN&Vr', '1982-03-09', 'suspended');
INSERT INTO users (name, username, email, user_password, date_of_birth, account_state) VALUES ('Mariana Lopez', 'mlopez22', 'mlopez22@example.com', 'xT7$Qw9!Lm', '1993-07-15', 'active');

--CAR script
SET search_path TO lyfter_car_rental;


CREATE TYPE car_state AS ENUM ('available', 'rented', 'maintenance', 'disabled');

CREATE TABLE cars(
  id SERIAL PRIMARY KEY,
  make VARCHAR(50) NOT NULL,
  model VARCHAR(50) NOT NULL,
  fabrication_year INT NOT NULL,
  state car_state NOT NULL
);

INSERT INTO cars (make, model, fabrication_year, state) VALUES ('Toyota', 'Corolla', 2020, 'available');
INSERT INTO cars (make, model, fabrication_year, state) VALUES ('Toyota', 'Camry', 2021, 'rented');
INSERT INTO cars (make, model, fabrication_year, state) VALUES ('Toyota', 'Hilux', 2019, 'maintenance');
INSERT INTO cars (make, model, fabrication_year, state) VALUES ('Honda', 'Civic', 2018, 'available');
INSERT INTO cars (make, model, fabrication_year, state) VALUES ('Honda', 'Accord', 2022, 'disabled');
INSERT INTO cars (make, model, fabrication_year, state) VALUES ('Honda', 'CR-V', 2021, 'available');
INSERT INTO cars (make, model, fabrication_year, state) VALUES ('Ford', 'Mustang', 2020, 'maintenance');
INSERT INTO cars (make, model, fabrication_year, state) VALUES ('Ford', 'F-150', 2019, 'available');
INSERT INTO cars (make, model, fabrication_year, state) VALUES ('Ford', 'Explorer', 2021, 'rented');
INSERT INTO cars (make, model, fabrication_year, state) VALUES ('Chevrolet', 'Malibu', 2019, 'available');
INSERT INTO cars (make, model, fabrication_year, state) VALUES ('Chevrolet', 'Silverado', 2022, 'disabled');
INSERT INTO cars (make, model, fabrication_year, state) VALUES ('Chevrolet', 'Spark', 2018, 'available');
INSERT INTO cars (make, model, fabrication_year, state) VALUES ('Nissan', 'Altima', 2021, 'available');
INSERT INTO cars (make, model, fabrication_year, state) VALUES ('Nissan', 'Sentra', 2020, 'rented');
INSERT INTO cars (make, model, fabrication_year, state) VALUES ('Nissan', 'Frontier', 2019, 'maintenance');
INSERT INTO cars (make, model, fabrication_year, state) VALUES ('Hyundai', 'Elantra', 2020, 'available');
INSERT INTO cars (make, model, fabrication_year, state) VALUES ('Hyundai', 'Tucson', 2021, 'disabled');
INSERT INTO cars (make, model, fabrication_year, state) VALUES ('Hyundai', 'Santa Fe', 2019, 'available');
INSERT INTO cars (make, model, fabrication_year, state) VALUES ('Kia', 'Sportage', 2020, 'available');
INSERT INTO cars (make, model, fabrication_year, state) VALUES ('Kia', 'Sorento', 2021, 'rented');
INSERT INTO cars (make, model, fabrication_year, state) VALUES ('Kia', 'Rio', 2018, 'available');
INSERT INTO cars (make, model, fabrication_year, state) VALUES ('Volkswagen', 'Golf', 2019, 'available');
INSERT INTO cars (make, model, fabrication_year, state) VALUES ('Volkswagen', 'Passat', 2020, 'disabled');
INSERT INTO cars (make, model, fabrication_year, state) VALUES ('Volkswagen', 'Tiguan', 2021, 'available');
INSERT INTO cars (make, model, fabrication_year, state) VALUES ('BMW', 'X5', 2021, 'maintenance');
INSERT INTO cars (make, model, fabrication_year, state) VALUES ('BMW', '3 Series', 2022, 'available');
INSERT INTO cars (make, model, fabrication_year, state) VALUES ('BMW', '5 Series', 2020, 'rented');
INSERT INTO cars (make, model, fabrication_year, state) VALUES ('Mercedes-Benz', 'C-Class', 2020, 'available');
INSERT INTO cars (make, model, fabrication_year, state) VALUES ('Mercedes-Benz', 'E-Class', 2021, 'disabled');
INSERT INTO cars (make, model, fabrication_year, state) VALUES ('Mercedes-Benz', 'GLA', 2019, 'available');
INSERT INTO cars (make, model, fabrication_year, state) VALUES ('Audi', 'A4', 2020, 'available');
INSERT INTO cars (make, model, fabrication_year, state) VALUES ('Audi', 'Q5', 2021, 'rented');
INSERT INTO cars (make, model, fabrication_year, state) VALUES ('Audi', 'A6', 2019, 'available');
INSERT INTO cars (make, model, fabrication_year, state) VALUES ('Mazda', 'Mazda3', 2020, 'available');
INSERT INTO cars (make, model, fabrication_year, state) VALUES ('Mazda', 'CX-5', 2021, 'disabled');
INSERT INTO cars (make, model, fabrication_year, state) VALUES ('Mazda', 'Mazda6', 2019, 'available');
INSERT INTO cars (make, model, fabrication_year, state) VALUES ('Subaru', 'Impreza', 2020, 'available');
INSERT INTO cars (make, model, fabrication_year, state) VALUES ('Subaru', 'Forester', 2021, 'maintenance');
INSERT INTO cars (make, model, fabrication_year, state) VALUES ('Subaru', 'Outback', 2019, 'available');
INSERT INTO cars (make, model, fabrication_year, state) VALUES ('Tesla', 'Model 3', 2021, 'available');
INSERT INTO cars (make, model, fabrication_year, state) VALUES ('Tesla', 'Model S', 2020, 'rented');
INSERT INTO cars (make, model, fabrication_year, state) VALUES ('Tesla', 'Model X', 2019, 'available');
INSERT INTO cars (make, model, fabrication_year, state) VALUES ('Peugeot', '208', 2020, 'available');
INSERT INTO cars (make, model, fabrication_year, state) VALUES ('Peugeot', '3008', 2021, 'disabled');
INSERT INTO cars (make, model, fabrication_year, state) VALUES ('Peugeot', '508', 2019, 'available');
INSERT INTO cars (make, model, fabrication_year, state) VALUES ('Renault', 'Clio', 2020, 'available');
INSERT INTO cars (make, model, fabrication_year, state) VALUES ('Renault', 'Captur', 2021, 'rented');
INSERT INTO cars (make, model, fabrication_year, state) VALUES ('Renault', 'Megane', 2019, 'available');
INSERT INTO cars (make, model, fabrication_year, state) VALUES ('Fiat', '500', 2020, 'available');
INSERT INTO cars (make, model, fabrication_year, state) VALUES ('Fiat', 'Panda', 2021, 'maintenance');


-- Intermediate table script

SET search_path TO lyfter_car_rental;

CREATE TYPE rent_car_state AS ENUM ('pending','active','completed','cancelled','overdue');

CREATE TABLE users_cars(
  id SERIAL PRIMARY KEY,
  user_id INT REFERENCES users(id) NOT NUll,
  car_id  INT REFERENCES cars(id) NOT NULL,
  rent_date DATE DEFAULT CURRENT_DATE NOT NULL,
  rent_status rent_car_state NOT NULL
);


INSERT INTO users_cars (user_id, car_id, rent_date, rent_status) VALUES (1, 5, '2026-01-15', 'completed');
INSERT INTO users_cars (user_id, car_id, rent_date, rent_status) VALUES (2, 12, '2026-02-03', 'pending');
INSERT INTO users_cars (user_id, car_id, rent_date, rent_status) VALUES (3, 20, '2026-02-10', 'cancelled');
INSERT INTO users_cars (user_id, car_id, rent_date, rent_status) VALUES (4, 7, '2026-03-01', 'completed');
INSERT INTO users_cars (user_id, car_id, rent_date, rent_status) VALUES (5, 18, '2026-03-12', 'active');
INSERT INTO users_cars (user_id, car_id, rent_date, rent_status) VALUES (6, 25, '2026-04-05', 'completed');
INSERT INTO users_cars (user_id, car_id, rent_date, rent_status) VALUES (7, 30, '2026-04-20', 'cancelled');
INSERT INTO users_cars (user_id, car_id, rent_date, rent_status) VALUES (8, 9, '2026-05-02', 'active');
INSERT INTO users_cars (user_id, car_id, rent_date, rent_status) VALUES (9, 15, '2026-05-18', 'completed');
INSERT INTO users_cars (user_id, car_id, rent_date, rent_status) VALUES (10, 22, '2026-06-01', 'overdue');

-- Task 2

-- 1. 
INSERT INTO users (name, username, email, user_password, date_of_birth, account_state) VALUES ('Jim Raynor', 'RaynoR_J', 'jraynor20@mail.com', 'jD3bhY-I?8..GH,', '1998-03-23', 'active');

-- 2. 
INSERT INTO cars (make, model, fabrication_year, state) VALUES ('Toyota', 'Land Cruiser', 2024, 'available');

--3. 
UPDATE users SET account_state = 'active' WHERE id = 10;

--4.
UPDATE cars SET state = 'available' WHERE id = 5;

--5.  
CREATE OR REPLACE FUNCTION set_car_rented() RETURNS TRIGGER AS $$
BEGIN
	IF NEW.rent_status = 'active' or NEW.rent_status = 'pending' THEN
		Update cars
		SET state = 'rented'
		WHERE id = NEW.car_id;
	END IF;
	RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_set_car_rented
AFTER INSERT ON users_cars
FOR EACH ROW
EXECUTE FUNCTION set_car_rented();

INSERT INTO users_cars (user_id, car_id, rent_status) VALUES (11, 35, 'active');

--6.  
CREATE OR REPLACE FUNCTION set_car_available() RETURNS TRIGGER AS $$
BEGIN
	IF NEW.rent_status = 'completed' THEN
		Update cars
		SET state = 'available'
		WHERE id = NEW.car_id;
	END IF;
	RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_set_car_available
AFTER UPDATE ON users_cars
FOR EACH ROW
EXECUTE FUNCTION set_car_available();

UPDATE users_cars
SET rent_status = 'completed'
WHERE id = 11;

--7.
UPDATE cars
SET state = 'disabled'
WHERE id = 24;

--8.

SELECT * FROM cars
WHERE state = 'rented';

SELECT * FROM cars
WHERE state = 'available';