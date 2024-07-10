import redis
import os
import json

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

# Initialize the Redis client
redis_client = redis.Redis.from_url(REDIS_URL)

async def initialize():
    # Add any initialization logic for Redis if needed
    pass

async def close():
    # Add any cleanup logic for Redis if needed
    pass

def cache_response(key: str, value: dict, expiration: int = 3600):
    """Cache the given response data in Redis."""
    redis_client.set(key, json.dumps(value), ex=expiration)

def get_cached_response(key: str):
    """Retrieve the cached response data from Redis."""
    cached_data = redis_client.get(key)
    if cached_data:
        return json.loads(cached_data)
    return None
