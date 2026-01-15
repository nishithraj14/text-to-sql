import pandas as pd

def run_sql(engine, sql):
    try:
        return pd.read_sql_query(sql, engine)
    except Exception as e:
        return f"SQL Error: {e}"
