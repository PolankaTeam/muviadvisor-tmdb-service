from fastapi import APIRouter
from services.tmdb import *
from services.chromadbClient import ChromaDbClient

router = APIRouter()

@router.get('/api/chromadb/search/', tags=["movies"])
async def search(keyword: str, collectionName: str):
    chromaDbClient = ChromaDbClient()
    results = chromaDbClient.semanticSearchCollection(keyword, collectionName, 10)

    return results