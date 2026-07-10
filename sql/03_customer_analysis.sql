-- ==========================================
-- CUSTOMER ANALYSIS
-- ==========================================

-- Top Customers

SELECT
c.customer_id,
c.first_name,
c.last_name,
ROUND(SUM(oi.total_amount),2) total_spent
FROM customers c
JOIN orders o
ON c.customer_id=o.customer_id
JOIN order_items oi
ON o.order_id=oi.order_id
GROUP BY
c.customer_id,
c.first_name,
c.last_name
ORDER BY total_spent DESC
LIMIT 10;

-- Membership Distribution

SELECT
membership,
COUNT(*) total_customers
FROM customers
GROUP BY membership
ORDER BY total_customers DESC;