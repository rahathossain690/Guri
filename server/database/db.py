import os
import psycopg2

PG_HOST = os.environ.get("POSTGRES_HOST", "db")
PG_DB = os.environ.get("POSTGRES_DB", "postgres")
PG_USER = os.environ.get("POSTGRES_USER", "postgres")
PG_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "password69")

def get_connection():
    return psycopg2.connect(
        host=PG_HOST,
        dbname=PG_DB,
        user=PG_USER,
        password=PG_PASSWORD
    )

def execute_query(query, params=None):
    print(f"[DB] Executing query: {query}")
    if params:
        print(f"[DB] With params: {params}")
    conn = get_connection()
    cur = conn.cursor()
    try:
        if params is not None:
            if query.count('%s') != len(params):
                print(f"[DB][ERROR] Parameter count mismatch: {len(params)} params for {query.count('%s')} placeholders")
                raise ValueError(f"Parameter count ({len(params)}) does not match placeholders ({query.count('%s')})")
            cur.execute(query, params)
        else:
            cur.execute(query)
        conn.commit()
        print(f"[DB] Query executed successfully.")
    except Exception as e:
        print(f"[DB][ERROR] Error executing query: {query} with params: {params} - {e}")
        conn.rollback()
        raise
    finally:
        cur.close()
        conn.close() 