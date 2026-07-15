# 📊 AnalytixAI

AnalytixAI is an AI-powered Business Intelligence platform that enables users to analyze business data using natural language. Instead of writing SQL queries manually, users can simply ask questions in plain English, and the application generates SQL, retrieves data from a PostgreSQL database, creates interactive visualizations, and provides AI-generated business insights.

---

## 🎥 Demo Video

Watch the complete application walkthrough:

https://youtu.be/de9VpMaVzEE

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
## 🏗️ Architecture

```text
                 ┌──────────────────────────┐
                 │        User Query        │
                 └────────────┬─────────────┘
                              │
                              ▼
                 ┌──────────────────────────┐
                 │  Gemini SQL Generator    │
                 └────────────┬─────────────┘
                              │
                              ▼
                 ┌──────────────────────────┐
                 │     SQL Validation       │
                 └────────────┬─────────────┘
                              │
                              ▼
                 ┌──────────────────────────┐
                 │    PostgreSQL Database   │
                 └────────────┬─────────────┘
                              │
                    Query Results Returned
                              │
                ┌─────────────┴─────────────┐
                ▼                           ▼
      ┌──────────────────┐      ┌──────────────────┐
      │ Plotly Charts    │      │ Mistral Summary  │
      │ KPI & Analytics  │      │ Business Insights│
      └─────────┬────────┘      └─────────┬────────┘
                └─────────────┬───────────┘
                              ▼
                 ┌──────────────────────────┐
                 │   Streamlit Dashboard    │
                 └──────────────────────────┘
```

---

## 🛠️ Tech Stack

### Languages
- Python
- SQL

### AI & LLM
- LangChain
- Google Gemini
- Mistral AI

### Database
- PostgreSQL

### Data & Visualization
- Pandas
- Plotly Express

### Frontend
- Streamlit

---

## 📂 Project Structure

```text
AnalytixAI/
│
├── backend/
│   ├── database.py
│   ├── query_builder.py
│   ├── query_executor.py
│   └── sql_validator.py
│
├── data/
│   └── NovaMart_Starter_Dataset.xlsx
│
├── database/
│   ├── queries/
│   ├── schema/
│   │   └── create_tables.sql
│   └── seeds/
│       └── generate_data.py
│
├── llm/
│   ├── __init__.py
│   ├── llm.py
│   ├── prompts.py
│   ├── response_generator.py
│   └── sql_generator.py
│
├── sql/
│   ├── 01_KPI_queries.sql
│   ├── 02_sales_analysis.sql
│   ├── 03_customer_analysis.sql
│   └── 05_views.sql
│
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
├── streamlit_app.py
└── structure.txt
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


## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/vaibhaviimahajan/AnalytixAI.git
cd AnalytixAI
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GOOGLE_API_KEY=your_google_api_key
MISTRAL_API_KEY=your_mistral_api_key

DB_NAME=your_database
DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=your_host
DB_PORT=5432
```

Run the application:

```bash
streamlit run streamlit_app.py
```

---
## 📁 Dataset

The project uses a sample e-commerce dataset located in the `data/` directory.

To run the application locally:

1. Create a PostgreSQL database.
2. Import the dataset into PostgreSQL.
3. Update the database credentials in your `.env` file.
4. Launch the Streamlit application.

---

## 💡 Example Questions

- Which products generated the highest revenue?
- Show monthly sales trends.
- Which customers spent the most?
- What is the revenue by payment method?
- Which product category performs best?

---

