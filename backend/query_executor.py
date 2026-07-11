from backend.database import get_connection


def execute_query(query, params=None, return_columns=False):
    """
    Executes SQL and optionally returns column names.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(query, params)

    rows = cursor.fetchall()

    columns = [desc[0] for desc in cursor.description]

    cursor.close()
    conn.close()

    if return_columns:
        return rows, columns

    return rows 