from llm.llm import get_llm
from llm.prompts import SQL_PROMPT, DATABASE_SCHEMA

llm = get_llm()


def generate_sql(question):

    prompt = SQL_PROMPT.format(
        schema=DATABASE_SCHEMA,
        question=question
    )

    response = llm.invoke(prompt)

    sql = response.content.strip()

    sql = sql.replace("```sql", "")
    sql = sql.replace("```", "")
    sql = sql.strip()

    return sql