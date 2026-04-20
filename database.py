import os
import psycopg2
from psycopg2.extras import RealDictCursor

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
INSTANCE_CONNECTION_NAME = os.getenv("INSTANCE_CONNECTION_NAME")

def get_db_connection():
    return psycopg2.connect(
        user=DB_USER,
        password=DB_PASSWORD,
        dbname=DB_NAME,
        host=f"/cloudsql/{INSTANCE_CONNECTION_NAME}",
        cursor_factory=RealDictCursor
    )
