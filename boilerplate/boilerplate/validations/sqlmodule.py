import sqlalchemy as sa


def execute_query(source, column, client):
    connection = f"postgresql://{source.username}:{source.password}@" \
        f"{source.host}:{source.port}/{source.database}"
    engine = sa.create_engine(connection)
    query = sa.text(f"select {column} from {source.table} where id={client.id}")
    print(query)
    result = engine.execute(query).fetchone()[0]
    print(result)
    return result
