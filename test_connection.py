from backend.query_executor import execute_query

query = """
SELECT COUNT(*)
FROM customers;
"""

result = execute_query(query)

print(result)