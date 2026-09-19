import os

from dotenv import load_dotenv


load_dotenv()


def get_required_setting(name):
	value = os.getenv(name)
	if not value:
		raise RuntimeError(f"Missing required environment variable: {name}")
	return value


def get_database_settings():
	return {
		"host": os.getenv("POSTGRES_HOST"),
		"port": int(os.getenv("POSTGRES_PORT")),
        "dbname": os.getenv("POSTGRES_DB"),
		"user": os.getenv("POSTGRES_USER"),
		"password": os.getenv("POSTGRES_PASSWORD"),
		"connect_timeout": 10,
	}


def get_openai_api_key():
	return get_required_setting("OPENAI_API_KEY")