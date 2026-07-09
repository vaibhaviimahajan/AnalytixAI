CREATE TABLE categories (
    category_id SERIAL PRIMARY KEY,
    category_name VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    category_id INT NOT NULL,
    product_name VARCHAR(150) NOT NULL,
    brand VARCHAR(100),
    cost_price DECIMAL(10,2),
    selling_price DECIMAL(10,2),

    CONSTRAINT fk_category
        FOREIGN KEY (category_id)
        REFERENCES categories(category_id)
);

CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(150) UNIQUE,
    city VARCHAR(100),
    country VARCHAR(100),
    membership VARCHAR(20),
    join_date DATE
);

CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INT NOT NULL,
    order_date DATE,
    payment_method VARCHAR(30),
    order_status VARCHAR(30),

    CONSTRAINT fk_customer
        FOREIGN KEY(customer_id)
        REFERENCES customers(customer_id)
);

CREATE TABLE order_items (
    order_item_id SERIAL PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT,
    discount DECIMAL(5,2),
    total_amount DECIMAL(10,2),

    CONSTRAINT fk_order
        FOREIGN KEY(order_id)
        REFERENCES orders(order_id),

    CONSTRAINT fk_product
        FOREIGN KEY(product_id)
        REFERENCES products(product_id)
);