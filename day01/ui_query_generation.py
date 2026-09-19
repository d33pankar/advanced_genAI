import streamlit as st

from openai_client import get_openai_client
from query_generator import generate_sql
from query_repository import execute_read_only_query
from schema_repository import get_database_schema


@st.cache_resource
def get_client():
	return get_openai_client()


st.title("Database Query Assistant")
question = st.text_input("What data do you want?")

if st.button("Generate SQL") and question:
	with st.spinner("Generating SQL..."):
		st.session_state.generated_sql = generate_sql(
			get_client(), question, get_database_schema()
		)

if st.session_state.get("generated_sql"):
	st.code(st.session_state.generated_sql, language="sql")

	if st.button("Run SQL"):
		try:
			st.dataframe(execute_read_only_query(st.session_state.generated_sql))
		except ValueError as error:
			st.error(str(error))
