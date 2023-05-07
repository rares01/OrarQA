# Import necessary libraries
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def connection():
    conn = psycopg2.connect(
        host='localhost',
        port='5432',
        user='power-user',
        password='root',
        database='Orar'
    )

    # Set autocommit to true to avoid transaction issues
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    return conn


class DbContext:
    pass
