from llm.llm import get_llm

llm = get_llm()


def generate_response(question, sql, results):

    prompt = f"""
You are a business analyst.

User Question:
{question}

Generated SQL:
{sql}

Query Results:
{results}

Write a short, professional business summary.
Do not mention SQL.
Keep it under 120 words.
"""

    response = llm.invoke(prompt)

    return response.content