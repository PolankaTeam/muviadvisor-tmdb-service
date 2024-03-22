import httpx
import os

TMDB_API_KEY = '7e59b9c230ccf64f151e491af5554fcc'

    
async def fetch_movies(movie_id: int):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    params = {
        'api_key': TMDB_API_KEY,
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        response.raise_for_status()
        return response.json()

async def search_movie_by_keyword(keyword: str):
    url = "https://api.themoviedb.org/3/search/movie"
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

        # await add_movie_to_weaviate(results)

        return results






