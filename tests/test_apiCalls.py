import pytest
import os
from src.app.services.tmdb import fetch_movies

API_KEY = os.getenv("API_KEY")

def test_fetch_movie_details_return_type():
  mocked_movie_id = 100
  retval = fetch_movies(mocked_movie_id, API_KEY)
  assert isinstance(retval, dict)
