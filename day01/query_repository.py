import re

from database import get_connection


def validate_read_only_query(query):
    normalized_query = query.strip().rstrip(";").strip()
    if not re.match(r"^(select|with)\b", normalized_query, re.IGNORECASE):
        raise ValueError("Only SELECT or WITH queries are allowed.")
    if ";" in normalized_query:
        raise ValueError("Only one SQL statement is allowed.")
    if re.search(r"\b(insert|update|delete|drop|alter|truncate|create|grant|revoke)\b", normalized_query, re.IGNORECASE):
        raise ValueError("The query contains a disallowed SQL operation.")
    return normalized_query


def execute_read_only_query(query):
    validated_query = validate_read_only_query(query)
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(validated_query)
            return cursor.fetchall()
            