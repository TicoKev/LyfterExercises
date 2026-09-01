-- SQLite
CREATE TABLE cars(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  vin CHAR(11) UNIQUE NOT NULL,
  model_id INT REFERENCES models(id) NOT NUll,
  color_id INT REFERENCES colors(id) NOT NULL
);

CREATE TABLE models(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  model_name VARCHAR(25) NOT NULL,
  make_id INT REFERENCES makes(id) NOT NULL,
  year CHAR(4) NOT NULL
);

CREATE TABLE makes(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(20) NOT NULL
);


CREATE TABLE colors(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  color VARCHAR(30) NOT NULL
);


CREATE TABLE owners(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(30) NOT NUll,
  phone_number VARCHAR(20) NOT NUll
);

CREATE TABLE car_owners(
  car_id REFERENCES cars(id) NOT NULL,
  owner_id REFERENCES owners(id) NOT NULL,
  insurance_policy_id INT REFERENCES insurance_policies(id) NOT NULL,
  PRIMARY KEY(car_id, owner_id)
);


CREATE TABLE insurance_companies(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  insurance_company_name VARCHAR(35) NOT NULL
);


CREATE TABLE insurance_policies(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  policy_name VARCHAR(25),
  insurance_company_id INT REFERENCES insurance_companies(id) NOT NULL
);



--Justification for the Cars exercise

--Similar to the previous case, the first step was to analyze the original table and identify the main entities. In this case, the core entities were owners and cars.  
--After that, I separated attributes that conceptually belong to independent entities rather than the car itself, such as make, model, color, and year. This avoids 
--redundancy and ensures compliance with higher normal forms.  
--Next, I examined the relationship between cars and owners. Since a car can have multiple owners over time and an owner can possess multiple cars, this is an N:N relationship. 
--To represent it correctly, I created a cross table that connects cars and owners while also storing insurance details. This design guarantees that each attribute depends 
--on the full primary key and maintains data consistency.
