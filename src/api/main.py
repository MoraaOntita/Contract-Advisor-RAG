from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .endpoints import query, health

app = FastAPI()

# Include routes from endpoints
app.include_router(query.router, prefix="/query")
app.include_router(health.router, prefix="/health")

# Serve static files
app.mount("/static", StaticFiles(directory="src/api/static"), name="static")

# Define root route (optional)
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI server!"}
