# 📊 AnalytixAI

AnalytixAI is an AI-powered Business Intelligence platform that enables users to analyze business data using natural language. Instead of writing SQL queries manually, users can simply ask questions in plain English, and the application generates SQL, retrieves data from a PostgreSQL database, creates interactive visualizations, and provides AI-generated business insights.

---

## ✨ Features

- 💬 Natural Language to SQL using Mistral AI
- 🗄️ PostgreSQL database integration
- 🛡️ SQL query validation for safer execution
- 📈 Interactive dashboards with Plotly
- 📊 KPI cards for key business metrics
- 🔍 Dynamic dashboard filters
- 🤖 AI-generated business summaries
- 💻 Clean and interactive Streamlit interface

---

## 🛠️ Tech Stack

- Python
- Streamlit
- PostgreSQL
- LangChain
- Mistral AI
- Plotly
- Pandas
- Psycopg2

---

## 📂 Project Structure

```
AnalytixAI
│
├── backend/
│   ├── database.py
│   ├── query_executor.py
│   └── sql_validator.py
│
├── llm/
│   ├── llm.py
│   ├── prompts.py
│   ├── sql_generator.py
│   └── response_generator.py
│
├── streamlit_app.py
├── requirements.txt
└── README.md
```

---

## 🚀 How It Works

1. User asks a business question in natural language.
2. The LLM converts the question into an SQL query.
3. SQL Validator checks the generated query.
4. The query is executed on PostgreSQL.
5. Results are displayed in a table.
6. Plotly automatically generates interactive charts.
7. The AI produces a concise business summary based on the results.

---


## 💡 Example Questions

- Which products generated the highest revenue?
- Show monthly sales trends.
- Which customers spent the most?
- What is the revenue by payment method?
- Which product category performs best?

---

