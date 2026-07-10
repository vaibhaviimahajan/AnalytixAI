-- ==========================================
-- SALES ANALYSIS
-- ==========================================

-- Monthly Revenue

SELECT
DATE_TRUNC('month',order_date) AS month,
ROUND(SUM(oi.total_amount),2) revenue
FROM orders o
JOIN order_items oi
ON o.order_id=oi.order_id
GROUP BY month
ORDER BY month;

-- Revenue by Payment Method

SELECT
payment_method,
ROUND(SUM(oi.total_amount),2) revenue
FROM orders o
JOIN order_items oi
ON o.order_id=oi.order_id
GROUP BY payment_method
ORDER BY revenue DESC;

-- Revenue by Order Status

SELECT
order_status,
ROUND(SUM(oi.total_amount),2) revenue
FROM orders o
JOIN order_items oi
ON o.order_id=oi.order_id
GROUP BY order_status
ORDER BY revenue DESC;