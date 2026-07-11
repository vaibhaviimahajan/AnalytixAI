DATABASE_SCHEMA = """
Database: NovaMart

Tables:

categories
- category_id
- category_name

products
- product_id
- category_id
- product_name
- brand
- cost_price
- selling_price

customers
- customer_id
- first_name
- last_name
- email
- city
- country
- membership
- join_date

orders
- order_id
- customer_id
- order_date
- payment_method
- order_status
- total_amount

order_items
- order_item_id
- order_id
- product_id
- quantity
- discount
- total_amount
"""


SQL_PROMPT = """
You are an expert PostgreSQL SQL developer.

Use ONLY the schema below.

{schema}

Rules:
1. Return ONLY PostgreSQL SQL.
2. Never return markdown.
3. Never explain anything.
4. Only generate SELECT statements.
5. Use proper JOINs whenever required.
6. If the question cannot be answered, return NOT_POSSIBLE.

User Question:
{question}
"""