from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from prometheus_fastapi_instrumentator import Instrumentator
from .endpoints import query, health
from src.database.db import database
from src.database.redis import redis_client, cache_response, get_cached_response
import logging
import json

app = FastAPI()

# Instrumentation for Prometheus
Instrumentator().instrument(app).expose(app)

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

# Example endpoint using Redis caching
@app.get("/contract/{contract_id}")
async def get_contract(contract_id: int):
    # Try to get data from Redis cache
    cached_data = get_cached_response(f"contract:{contract_id}")
    if cached_data:
        return cached_data

    # If not in cache, fetch from database
    contract_data = fetch_contract_from_db(contract_id)
    
    # Store data in Redis cache
    cache_response(f"contract:{contract_id}", contract_data)
    
    return contract_data

def fetch_contract_from_db(contract_id):
    # Simulated database fetch function
    # You should replace this with actual database interaction logic
    return {"id": contract_id, "title": f"Contract {contract_id}", "content": "This is the content of the contract."}
