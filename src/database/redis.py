import redis
import os
from src.config import REDIS_URL

# Initialize the Redis client
redis_client = redis.Redis.from_url(REDIS_URL)

async def initialize():
    # Add any initialization logic for Redis if needed
    pass

async def close():
    # Add any cleanup logic for Redis if needed
    pass
