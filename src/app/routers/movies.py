from fastapi import APIRouter, Depends, HTTPException
from services.tmdb import *
from services.chromadbClient import ChromaDbClient

router = APIRouter()

@router.get("/test", tags=["movies"])
async def test():
    return {"message": "Test message"}

@router.get('/movies/search/id={movie_id}', tags=["movies"])
async def fetch(movie_id: int):
    return await fetch_movies(movie_id)

@router.get('/movies/search/keyword={keyword}', tags=["movies"])
async def search(keyword: str):
    data = await search_movie_by_keyword(keyword)
    chromaDbClient = ChromaDbClient()
    chromaDbClient.populateColletionWithDataFromTMDB("Test", data)
    
    return data


