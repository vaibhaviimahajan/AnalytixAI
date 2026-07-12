from llm.llm import get_llm

llm = get_llm()


def generate_response(question, sql, results):

    results_text = "\n".join(str(row) for row in results)

    prompt = f"""
You are an experienced business analyst.

Question:
{question}

Results:
{results_text}

Write a plain English summary.
Do not use Markdown.
Do not use bold.
Do not use bullets.
Keep it under 100 words.
"""

    response = llm.invoke(prompt)

    print("\n========== MISTRAL RESPONSE ==========\n")
    print(response.content)
    print("\n======================================\n")

    return response.content