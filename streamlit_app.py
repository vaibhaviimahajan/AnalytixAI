import streamlit as st
import pandas as pd
import plotly.express as px
from backend.query_executor import execute_query
from llm.sql_generator import generate_sql
from llm.response_generator import generate_response
from backend.sql_validator import validate_sql

st.set_page_config(
    page_title="AnalytixAI",
    page_icon="📊",
    layout="wide"
)

if "messages" not in st.session_state:
    st.session_state.messages = []

st.sidebar.title("📊 Dashboard Filters")
categories = execute_query("""
SELECT category_name
FROM categories
ORDER BY category_name;
""")

category_list = ["All"] + [row[0] for row in categories]

selected_category = st.sidebar.selectbox(
    "Select Category",
    category_list
)

payments = execute_query("""
SELECT DISTINCT payment_method
FROM orders
ORDER BY payment_method;
""")

payment_list = ["All"] + [row[0] for row in payments]

selected_payment = st.sidebar.selectbox(
    "Payment Method",
    payment_list
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

if selected_category == "All":

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

else:

    monthly_sales = execute_query("""
        SELECT
            DATE_TRUNC('month', o.order_date) AS month,
            ROUND(SUM(oi.total_amount), 2) AS revenue
        FROM orders o
        JOIN order_items oi
            ON o.order_id = oi.order_id
        JOIN products p
            ON oi.product_id = p.product_id
        JOIN categories c
            ON p.category_id = c.category_id
        WHERE c.category_name = %s
        GROUP BY month
        ORDER BY month;
    """, (selected_category,))

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

st.subheader("💳 Revenue by Payment Method")


if selected_payment == "All":

    payment_data = execute_query("""
    SELECT
        payment_method,
        ROUND(SUM(oi.total_amount),2) AS revenue
    FROM orders o
    JOIN order_items oi
        ON o.order_id = oi.order_id
    GROUP BY payment_method
    ORDER BY revenue DESC;
    """)

else:

    payment_data = execute_query("""
    SELECT
        payment_method,
        ROUND(SUM(oi.total_amount),2) AS revenue
    FROM orders o
    JOIN order_items oi
        ON o.order_id = oi.order_id
    WHERE payment_method = %s
    GROUP BY payment_method
    ORDER BY revenue DESC;
    """, (selected_payment,))

df_payment = pd.DataFrame(
    payment_data,
    columns=["Payment Method", "Revenue"]
)

fig_payment = px.pie(
    df_payment,
    names="Payment Method",
    values="Revenue",
    hole=0.4,
    title="Revenue Distribution by Payment Method"
)

st.plotly_chart(fig_payment, use_container_width=True)

st.sidebar.subheader("📅 Date Range")

start_date = st.sidebar.date_input(
    "Start Date",
    value=pd.to_datetime("2025-01-01")
)

end_date = st.sidebar.date_input(
    "End Date",
    value=pd.Timestamp.today()
)

st.subheader("🏆 Top 10 Products")

product_data = execute_query("""
SELECT
    p.product_name,
    ROUND(SUM(oi.total_amount),2) AS revenue
FROM products p
JOIN order_items oi
ON p.product_id = oi.product_id
GROUP BY p.product_name
ORDER BY revenue DESC
LIMIT 10;
""")

df_products = pd.DataFrame(
    product_data,
    columns=["Product", "Revenue"]
)

fig_products = px.bar(
    df_products,
    x="Product",
    y="Revenue",
    title="Top Products by Revenue"
)

st.plotly_chart(fig_products, use_container_width=True)

st.subheader("👑 Top Customers")

customer_data = execute_query("""
SELECT
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
    ROUND(SUM(oi.total_amount),2) AS total_spent
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
JOIN order_items oi
ON o.order_id = oi.order_id
GROUP BY customer_name
ORDER BY total_spent DESC
LIMIT 10;
""")

df_customers = pd.DataFrame(
    customer_data,
    columns=["Customer", "Total Spent"]
)

fig_customers = px.bar(
    df_customers,
    x="Customer",
    y="Total Spent",
    title="Top Customers"
)

st.plotly_chart(fig_customers, use_container_width=True)

st.divider()

st.header("🤖 AI Business Assistant")

# Show previous conversation
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

st.markdown("""
### 💡 Try asking:
- What percentage of revenue comes from each product category?
- Show monthly sales trends.
- Who are the top 10 customers?
- What is the distribution of orders by payment method?
- Display weekly order count.
""")

user_question = st.chat_input(
    "Ask anything about your business..."
)

if user_question:

    # Save user's question
    st.session_state.messages.append({
        "role": "user",
        "content": user_question
    })

    with st.spinner("Analyzing your business data..."):

        try:
            sql = generate_sql(user_question)

            validate_sql(sql)

            with st.expander("📝 Generated SQL"):
                st.code(sql, language="sql")

            rows, columns = execute_query(
                sql,
                return_columns=True
            )

            df = pd.DataFrame(
                rows,
                columns=columns
            )
            st.dataframe(df, use_container_width=True)
            csv = df.to_csv(index=False).encode("utf-8")

            st.download_button(
                "📥 Download Results",
                csv,
                "query_results.csv",
                "text/csv"
            )
            if len(df.columns) >= 2:

                numeric_col = df.columns[-1]
                label_col = df.columns[-2]

                try:

                    df[numeric_col] = pd.to_numeric(df[numeric_col])

                    # Convert dates if possible
                    try:
                        df[label_col] = pd.to_datetime(df[label_col])
                    except:
                        pass

                    # Decide chart type
                    if pd.api.types.is_datetime64_any_dtype(df[label_col]):

                        fig = px.line(
                            df,
                            x=label_col,
                            y=numeric_col,
                            markers=True,
                            title="AI Generated Visualization"
                        )

                    elif "payment" in label_col.lower():

                        fig = px.pie(
                            df,
                            names=label_col,
                            values=numeric_col,
                            hole=0.4,
                            title="AI Generated Visualization"
                        )

                    else:

                        fig = px.bar(
                            df,
                            x=label_col,
                            y=numeric_col,
                            title="AI Generated Visualization"
                        )

                    st.plotly_chart(fig, use_container_width=True)

                except Exception:
                    pass

            # Save AI response
            summary = generate_response(
                user_question,
                sql,
                rows
            )
            

            st.subheader("AI Summary")
            st.write(summary)

        except Exception as e:
            st.error(str(e))

