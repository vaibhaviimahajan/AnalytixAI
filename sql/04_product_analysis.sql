-- ==========================================
-- PRODUCT ANALYSIS
-- ==========================================

-- Top Selling Products

SELECT
p.product_name,
SUM(oi.quantity) units_sold,
ROUND(SUM(oi.total_amount),2) revenue
FROM products p
JOIN order_items oi
ON p.product_id=oi.product_id
GROUP BY p.product_name
ORDER BY revenue DESC
LIMIT 10;

-- Top Brands

SELECT
brand,
ROUND(SUM(oi.total_amount),2) revenue
FROM products p
JOIN order_items oi
ON p.product_id=oi.product_id
GROUP BY brand
ORDER BY revenue DESC;