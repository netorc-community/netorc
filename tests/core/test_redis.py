import redis

from settings import settings


def test_redis_connection():
    conn = redis.from_url(settings.redis)
    conn.ping()
