import httpx
import os

TMDB_API_KEY = os.getenv("TMDB_API_KEY")
    
async def fetch_movies(movie_id: int):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US&page=1"
    params = {
        'api_key': TMDB_API_KEY,
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        response.raise_for_status()

        return response.json()

async def search_movie_by_keyword(keyword: str):
    url = "https://api.themoviedb.org/3/search/movie?language=en-US&page=1"
    params = {
        'api_key': TMDB_API_KEY,
        "query": keyword,
        "language": "en-US",
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        results = data.get("results", [])

        return results
    

async def similar_movies(movie_id: int):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/similar?language=en-US&page=1"
    params = {
        'api_key': TMDB_API_KEY,
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        results = data.get("results", [])
        
        return results
    
async def search_by_people(actorName: str):
    url = f"https://api.themoviedb.org/3/search/person?query={actorName}&language=en-US"
    params = {
        'api_key': TMDB_API_KEY,
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        results = data.get("results", [])
        
        return results







