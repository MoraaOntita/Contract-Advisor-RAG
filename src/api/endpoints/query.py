from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.rag_pipeline import generate_response, retrieve_relevant_context

router = APIRouter()

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    response: str  # Ensure this matches models.py

@router.post("/query", response_model=QueryResponse)
async def handle_query(request: QueryRequest):
    try:
        relevant_contexts = retrieve_relevant_context(request.query)
        answer = generate_response(request.query, relevant_contexts)
        return QueryResponse(response=answer)  # Ensure this uses 'response'
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
