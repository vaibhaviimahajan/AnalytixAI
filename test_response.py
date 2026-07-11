from llm.sql_generator import generate_sql
from llm.response_generator import generate_response
from backend.query_executor import execute_query

question = "Show top 5 products by revenue"

sql = generate_sql(question)

rows = execute_query(sql)

answer = generate_response(question, sql, rows)

print(answer)