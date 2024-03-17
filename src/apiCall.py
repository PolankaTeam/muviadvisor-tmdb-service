import requests

def fetch_movie_details(movie_id, api_key):
    """Fetches movie details from TMDb."""
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    parameters = {
        "api_key": api_key,
        "language": "en-US"
    }
    response = requests.get(url, params=parameters)
    if response.status_code == 200:
        return response.json()
    else:
        return None



