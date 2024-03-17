from fastapi import FastAPI
from apiCall import fetch_movie_details

app = FastAPI()


@app.get("/apiCall")
async def root():
    api_key = "7e59b9c230ccf64f151e491af5554fcc"
    movie_id = 550 # Example movie ID: Fight Club
    movie_details = fetch_movie_details(movie_id, api_key)
    if movie_details:
        return movie_details
    else:
        return "Failed to fetch movie details."