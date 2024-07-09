from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .endpoints import query, health
from src.database.db import database
from src.database.redis import redis_client
import logging

app = FastAPI()

@app.on_event("startup")
async def startup():
    # Connect to the database
    logging.info("Connecting to the database...")
    await database.connect()
    logging.info("Connected to the database.")
    # Check if Redis is reachable
    logging.info("Pinging Redis...")
    if not redis_client.ping():
        raise Exception("Could not connect to Redis")
    logging.info("Connected to Redis.")

@app.on_event("shutdown")
async def shutdown():
    # Disconnect from the database
    logging.info("Disconnecting from the database...")
    await database.disconnect()
    logging.info("Disconnected from the database.")

# Include routers for different endpoints
app.include_router(query.router, prefix="/query")
app.include_router(health.router, prefix="/health")

# Serve static files from the directory
app.mount("/static", StaticFiles(directory="src/api/static"), name="static")

# Define a root route for the server
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI server!"}
