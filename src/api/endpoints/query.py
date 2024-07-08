from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.rag_pipeline import generate_response, retrieve_relevant_context
import asyncio

router = APIRouter()

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    answer: str

@router.post("/query", response_model=QueryResponse)
async def handle_query(request: QueryRequest):
    try:
        # Asynchronously retrieve relevant context
        relevant_contexts = await asyncio.to_thread(retrieve_relevant_context, request.query)
        
        # Asynchronously generate a response
        answer = await asyncio.to_thread(generate_response, request.query, relevant_contexts)
        
        return QueryResponse(answer=answer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
