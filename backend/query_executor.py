from backend.database import get_connection


def execute_query(query, params=None):
    """
    Executes a SQL query and returns all rows.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(query, params)

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows