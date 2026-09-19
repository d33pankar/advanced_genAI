import psycopg

from config import get_database_settings


def get_connection():
    return psycopg.connect(**get_database_settings())