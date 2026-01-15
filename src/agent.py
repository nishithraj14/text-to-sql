import pandas as pd
from sqlalchemy import text
from .sql_generator import generate_sql

def agentic_query(schema, engine, question):
    sql = generate_sql(schema, question)
    with engine.connect() as conn:
        df = pd.read_sql(text(sql), conn)
    return sql, df
