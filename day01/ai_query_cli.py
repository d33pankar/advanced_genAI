from openai_client import get_openai_client
from query_generator import generate_sql
from schema_repository import get_database_schema


def main():
    question = input("\nWhat data do you want? ").strip()
    schema = get_database_schema()
    sql = generate_sql(get_openai_client(), question, schema)
    print("\n",sql, sep="", end="\n\n")


if __name__ == "__main__":
    main()