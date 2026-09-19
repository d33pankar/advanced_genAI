def generate_sql(client, question, schema):
    response = client.responses.create(
        model="gpt-4o-mini",
        input=f"""
                Generate one PostgreSQL SELECT query for the user's question.
                Return only SQL, with no markdown fences or explanation.

                Database schema:
                {schema}

                User question:
                {question}
                """,
    )
    return response.output_text.strip()