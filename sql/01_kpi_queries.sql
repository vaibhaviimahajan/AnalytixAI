-- ==========================================
-- KEY PERFORMANCE INDICATORS (KPIs)
-- ==========================================

-- Total Revenue
SELECT
ROUND(SUM(total_amount),2) AS total_revenue
FROM order_items;

-- Total Orders
SELECT
COUNT(*) AS total_orders
FROM orders;

-- Total Customers
SELECT
COUNT(*) AS total_customers
FROM customers;

-- Total Products
SELECT
COUNT(*) AS total_products
FROM products;

-- Average Order Value
SELECT
ROUND(
SUM(oi.total_amount)/COUNT(DISTINCT o.order_id),2
) AS average_order_value
FROM orders o
JOIN order_items oi
ON o.order_id=oi.order_id;