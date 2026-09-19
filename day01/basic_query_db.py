from schema_repository import get_table_schema, list_tables


def main():
    tables = list_tables()
    print("\nTables in the database:")
    print("-"*15)
    for table_name in tables:
        print(table_name)

    table_name = input("\n\nEnter a table name to view its schema: ").strip()
    if table_name not in tables:
        raise ValueError(f"Unknown table: {table_name}")

    print(f"Schema for table '{table_name}':",end="\n")
    print("-"*15)
    for column_name, data_type in get_table_schema(table_name):
        print(f"{column_name}: {data_type}")
    print("\n")

if __name__ == "__main__":
    main()