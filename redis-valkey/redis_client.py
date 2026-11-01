import redis


class RedisClient:
    def __init__(self):
        pool = redis.ConnectionPool()
        self.client = redis.Redis(
            host="127.0.0.1",
            port="6379",
            db=0,
        )
