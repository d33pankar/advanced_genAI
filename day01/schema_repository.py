from database import get_connection


def list_tables():
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT table_name
                FROM information_schema.tables
                WHERE table_schema = 'public'
                ORDER BY table_name;
            """)
            return [row[0] for row in cursor.fetchall()]


def get_table_schema(table_name):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT column_name, data_type
                FROM information_schema.columns
                WHERE table_schema = 'public'
                  AND table_name = %s
                ORDER BY ordinal_position;
            """, (table_name,))
            return cursor.fetchall()


def get_database_schema():
    return {
        table_name: get_table_schema(table_name)
        for table_name in list_tables()
    }