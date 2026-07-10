import streamlit as st
import pandas as pd
import plotly.express as px
from backend.query_executor import execute_query

st.set_page_config(
    page_title="AnalytixAI",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AnalytixAI")
st.caption("AI-Powered Business Analytics Platform")

# -------------------------
# Fetch KPIs
# -------------------------

total_revenue = execute_query("""
SELECT ROUND(SUM(total_amount),2)
FROM order_items;
""")[0][0]

total_orders = execute_query("""
SELECT COUNT(*)
FROM orders;
""")[0][0]

total_customers = execute_query("""
SELECT COUNT(*)
FROM customers;
""")[0][0]

total_products = execute_query("""
SELECT COUNT(*)
FROM products;
""")[0][0]

avg_order_value = execute_query("""
SELECT ROUND(
SUM(oi.total_amount)/COUNT(DISTINCT o.order_id),2
)
FROM orders o
JOIN order_items oi
ON o.order_id = oi.order_id;
""")[0][0]

# -------------------------
# KPI Cards
# -------------------------

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("💰 Revenue", f"₹ {total_revenue:,.2f}")
col2.metric("🛒 Orders", total_orders)
col3.metric("👥 Customers", total_customers)
col4.metric("📦 Products", total_products)
col5.metric("📈 Avg Order", f"₹ {avg_order_value:,.2f}")

st.divider()
st.subheader("📈 Monthly Revenue Trend")

monthly_sales = execute_query("""
SELECT
    DATE_TRUNC('month', o.order_date) AS month,
    ROUND(SUM(oi.total_amount), 2) AS revenue
FROM orders o
JOIN order_items oi
ON o.order_id = oi.order_id
GROUP BY month
ORDER BY month;
""")

df_monthly = pd.DataFrame(
    monthly_sales,
    columns=["Month", "Revenue"]
)

fig = px.line(
    df_monthly,
    x="Month",
    y="Revenue",
    markers=True,
    title="Monthly Revenue"
)

st.plotly_chart(fig, use_container_width=True)

st.info("📌 Dashboard charts coming in the next step.")