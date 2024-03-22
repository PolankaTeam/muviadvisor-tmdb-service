from fastapi import APIRouter, Depends, HTTPException
from services.tmdb import *
from services.chromadbClient import ChromaDbClient

router = APIRouter()

@router.get('/chromadb/search/keyword={keyword}', tags=["movies"])
async def search(keyword: str):
    chromaDbClient = ChromaDbClient()
    results = chromaDbClient.semanticSearchCollection(keyword,"Test", 10)
    return results