from sqlalchemy import inspect

def get_schema(engine):
    inspector = inspect(engine)
    schema = []

    for table in inspector.get_table_names():
        columns = inspector.get_columns(table)
        cols = [c["name"] for c in columns]
        schema.append(f"{table}: {cols}")

    return "\n".join(schema)
