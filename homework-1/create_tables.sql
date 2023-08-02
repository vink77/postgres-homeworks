CREATE TABLE employees
(
    employee_id integer PRIMARY KEY,
    first_name varchar(50) NOT NULL,
	last_name varchar(50) NOT NULL,
	title varchar(100) NOT NULL,
	birth_date date,
    notes text
);

CREATE TABLE customers
(
    customer_id varchar(100) PRIMARY KEY,
    company_name varchar(100),
	contact_name varchar(100)

);

CREATE TABLE orders
(
    order_id int PRIMARY KEY,
	customer_id varchar REFERENCES customers(customer_id) NOT NULL,
	employee_id integer REFERENCES employees(employee_id) NOT NULL,
	order_date date,
	ship_city varchar(100)
);
