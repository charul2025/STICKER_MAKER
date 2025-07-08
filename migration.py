import psycopg2
from dotenv import load_dotenv
import os
load_dotenv()  # take environment variables

# Migration SQL: create users table
migration_sql = """
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);
"""

def run_migration():
    try:
        conn = psycopg2.connect(
        os.getenv("DB_URL")
        )
        conn.autocommit = True
        cur = conn.cursor()
        cur.execute(migration_sql)
        print("Migration applied successfully.")
        cur.close()
        conn.close()
    except Exception as e:
        print("Migration failed:", e)

if __name__ == "__main__":
    run_migration()
