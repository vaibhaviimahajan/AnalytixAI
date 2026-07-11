from llm.sql_generator import generate_sql
from backend.query_executor import execute_query

question = "Show top 5 products by revenue"

sql = generate_sql(question)

print("\nGenerated SQL:\n")
print(sql)

print("\nResults:\n")

rows = execute_query(sql)

for row in rows:
    print(row)