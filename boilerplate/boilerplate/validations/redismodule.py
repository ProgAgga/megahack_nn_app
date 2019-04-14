# redis.hget(<user_id>, <field>)
from redis import Redis


def execute_query(source, column, client):
    r = Redis(host=source.host, port=source.port, db=source.database)
    result = r.hget(client.id, column)
    try:
        result = int(result)
    except (TypeError, ValueError):
        return None
    return result
