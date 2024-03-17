from fastapi import FastAPI, HTTPException
from apiCall import *
import uvicorn

app = FastAPI()


@app.get("/queryById")
async def root():
    api_key = "7e59b9c230ccf64f151e491af5554fcc"
    movie_id = 100 # Example movie ID: Fight Club
    movie_details = fetch_movie_details(movie_id, api_key)
    if movie_details:
        return movie_details
    else:
        return "Failed to fetch movie details."

@app.get("/queryByMovie")
async def query_by_movie(query: str):
    api_key = "7e59b9c230ccf64f151e491af5554fcc"
    movies = search_movie_by_keywords(api_key, query)
    if movies:
        return movies
    else:
        return "Failed to fetch movie details."
    
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

