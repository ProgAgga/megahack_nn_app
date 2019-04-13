# redis.hget(<user_id>, <field>)
from redis import Redis


def execute_query(source, table, column, client):
    connection = f"postgresql://{source.user}{source.password}@" \
        f"{source.host}:{source.port}/{source.database}"
    engine = sa.create_engine(connection)
    query = sa.text(f"select {column} from {table} where id={client.id}")
    result = engine.execute(query)
    print(result)
