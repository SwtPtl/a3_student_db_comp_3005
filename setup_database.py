import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

DB_NAME = 'assignment_4_db'  # db you're using for testing
DB_USER = 'postgres' # your username
DB_PASSWORD = '12345' # your passwd
DB_HOST = 'localhost'     # host config
SQL_FILE = 'setup_students.sql'

# Step 1: Connect to default db, create assignment db if needed
def create_db():
    conn = psycopg2.connect(dbname='postgres', user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    cur.execute(f"SELECT 1 FROM pg_database WHERE datname = '{DB_NAME}'")
    exists = cur.fetchone()
    if not exists:
        cur.execute(f'CREATE DATABASE {DB_NAME};')
        print(f"Database '{DB_NAME}' created.")
    else:
        print(f"Database '{DB_NAME}' already exists.")
    cur.close()
    conn.close()

# Step 2: Connect to assignment db, execute SQL script
def run_sql():
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
    cur = conn.cursor()
    with open(SQL_FILE, 'r') as f:
        sql = f.read()
        cur.execute(sql)
        conn.commit()
    print("Schema and initial data loaded.")
    cur.close()
    conn.close()

if __name__ == '__main__':
    create_db()
    run_sql()
