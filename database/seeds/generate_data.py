import os
import random
from datetime import date, timedelta

import psycopg2
from dotenv import load_dotenv
from faker import Faker

# -----------------------------
# Load Environment Variables
# -----------------------------
load_dotenv()

# -----------------------------
# Database Connection
# -----------------------------
conn = psycopg2.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT")
)

cursor = conn.cursor()
fake = Faker()

print("✅ Connected to PostgreSQL!")

# -----------------------------
# Clean Existing Data
# -----------------------------
cursor.execute("""
TRUNCATE TABLE order_items, orders, customers
RESTART IDENTITY CASCADE;
""")

conn.commit()

print("✅ Old data cleared!")

# -----------------------------
# Categories
# -----------------------------
categories = [
    "Electronics",
    "Fashion",
    "Home & Kitchen",
    "Beauty",
    "Sports",
    "Grocery"
]

for category in categories:
    cursor.execute("""
        INSERT INTO categories(category_name)
        VALUES (%s)
        ON CONFLICT(category_name) DO NOTHING
    """, (category,))

conn.commit()

print("✅ Categories inserted!")

# -----------------------------
# Products
# -----------------------------
products = [
    (1, "Laptop", "Dell", 55000, 65000),
    (1, "Smartphone", "Samsung", 30000, 38000),
    (1, "Wireless Earbuds", "Boat", 1500, 2499),
    (1, "Smart Watch", "Noise", 2500, 3999),
    (1, "Bluetooth Speaker", "JBL", 3500, 4999),

    (2, "Men's T-Shirt", "Levi's", 500, 999),
    (2, "Women's Jeans", "Levi's", 1200, 2499),
    (2, "Running Shoes", "Nike", 3500, 5999),
    (2, "Hoodie", "Puma", 1500, 2999),
    (2, "Casual Shirt", "US Polo", 900, 1799),

    (3, "Microwave Oven", "LG", 6000, 8999),
    (3, "Mixer Grinder", "Prestige", 2200, 3499),
    (3, "Dining Chair", "IKEA", 1800, 2999),
    (3, "Water Bottle", "Milton", 250, 499),
    (3, "Coffee Maker", "Philips", 3500, 4999),

    (4, "Face Wash", "Nivea", 120, 249),
    (4, "Shampoo", "Loreal", 280, 499),
    (4, "Perfume", "Bella Vita", 600, 1299),

    (5, "Cricket Bat", "SG", 2200, 3499),
    (5, "Football", "Adidas", 900, 1599),

    (6, "Basmati Rice 5kg", "India Gate", 450, 699),
    (6, "Green Tea", "Lipton", 180, 299),
    (6, "Coffee Powder", "Nescafe", 250, 399)
]

for product in products:
    cursor.execute("""
        INSERT INTO products
        (
            category_id,
            product_name,
            brand,
            cost_price,
            selling_price
        )
        VALUES (%s,%s,%s,%s,%s)
        ON CONFLICT DO NOTHING
    """, product)

conn.commit()

print("✅ Products inserted!")

# -----------------------------
# Customers
# -----------------------------
memberships = ["Bronze", "Silver", "Gold"]

for _ in range(100):

    cursor.execute("""
        INSERT INTO customers
        (
            first_name,
            last_name,
            email,
            city,
            country,
            membership,
            join_date
        )
        VALUES (%s,%s,%s,%s,%s,%s,%s)
    """, (
        fake.first_name(),
        fake.last_name(),
        fake.unique.email(),
        fake.city(),
        fake.country(),
        random.choice(memberships),
        date.today() - timedelta(days=random.randint(30, 1500))
    ))

conn.commit()

print("✅ Customers inserted!")

# -----------------------------
# Fetch IDs
# -----------------------------
cursor.execute("SELECT customer_id FROM customers")
customer_ids = [row[0] for row in cursor.fetchall()]

cursor.execute("SELECT product_id, selling_price FROM products")
products_data = cursor.fetchall()

print("✅ IDs loaded!")

# -----------------------------
# Orders + Order Items
# -----------------------------
payment_methods = [
    "Credit Card",
    "Debit Card",
    "UPI",
    "Net Banking"
]

order_statuses = [
    "Delivered",
    "Shipped",
    "Processing",
    "Cancelled"
]

for _ in range(500):

    customer_id = random.choice(customer_ids)

    cursor.execute("""
        INSERT INTO orders
        (
            customer_id,
            order_date,
            payment_method,
            order_status
        )
        VALUES (%s,%s,%s,%s)
        RETURNING order_id
    """, (
        customer_id,
        fake.date_between(start_date="-365d", end_date="today"),
        random.choice(payment_methods),
        random.choice(order_statuses)
    ))

    order_id = cursor.fetchone()[0]

    number_of_items = random.randint(1, 4)

    selected_products = random.sample(
        products_data,
        min(number_of_items, len(products_data))
    )

    for product in selected_products:

        product_id = product[0]
        selling_price = float(product[1])

        quantity = random.randint(1, 3)

        discount = random.choice([
            0,
            5,
            10,
            15
        ])

        total_amount = round(
            quantity *
            selling_price *
            (1 - discount / 100),
            2
        )

        cursor.execute("""
            INSERT INTO order_items
            (
                order_id,
                product_id,
                quantity,
                discount,
                total_amount
            )
            VALUES (%s,%s,%s,%s,%s)
        """, (
            order_id,
            product_id,
            quantity,
            discount,
            total_amount
        ))

conn.commit()

print("✅ Orders inserted!")
print("✅ Order items inserted!")

cursor.close()
conn.close()

print("🎉 NovaMart database generated successfully!")