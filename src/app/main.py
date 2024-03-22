from fastapi import FastAPI, HTTPException
from services.apiCall import *
import uvicorn
import os

app = FastAPI()

@app.get("/queryById")
async def query_by_id(id: int):
    api_key = os.getenv('TMDB_API_KEY')
    movie_details = fetch_movie_details(id, api_key)
    if movie_details:
        return movie_details
    else:
        return "Failed to fetch movie details."

@app.get("/freeTextSearch")
async def query_by_movie(query: str):
    api_key = os.getenv('TMDB_API_KEY')
    movies = search_movie_by_keywords(api_key, query)
    if movies:
        return movies
    else:
        return api_key
    
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

