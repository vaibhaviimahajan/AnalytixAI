def validate_sql(sql: str):
    sql = sql.strip().lower()

    forbidden = [
        "insert",
        "update",
        "delete",
        "drop",
        "alter",
        "truncate",
        "create",
        "grant",
        "revoke"
    ]

    if not sql.startswith("select"):
        raise Exception("Only SELECT queries are allowed.")

    for keyword in forbidden:
        if keyword in sql:
            raise Exception(f"Forbidden SQL detected: {keyword}")

    return True