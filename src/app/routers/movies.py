from fastapi import APIRouter
from services.tmdb import *
from services.chromadbClient import ChromaDbClient

router = APIRouter()

@router.get('/api/movies/search/id={movie_id}', tags=["movies"])
async def fetch(movie_id: int):
    return await fetch_movies(movie_id)

@router.get('/api/movies/search/', tags=["movies"])
async def search(keyword: str, collectionName: str):
    data = await search_movie_by_keyword(keyword)
    chromaDbClient = ChromaDbClient()
    chromaDbClient.populateColletionWithDataFromTMDB(collectionName, data)

    return data

@router.get('/api/movies/similar/', tags=["movies"])
async def search(movieId: int, collectionName: str):
    data = await similar_movies(movieId)
    chromaDbClient = ChromaDbClient()
    chromaDbClient.populateColletionWithDataFromTMDB(collectionName, data)

    return data

@router.get('/api/movies/people/', tags=["movies"])
async def search(actorName: str, collectionName: str):
    data = await search_by_people(actorName)
    chromaDbClient = ChromaDbClient()
    chromaDbClient.populateColletionWithDataFromTMDB(collectionName, data)

    return data



