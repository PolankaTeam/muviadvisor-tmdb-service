import pytest
import os
from src.app.services.apiCall import fetch_movie_details

API_KEY = os.getenv("TMDB_API_KEY")

def test_fetch_movie_details_return_type():
  mocked_movie_id = 100
  retval = fetch_movie_details(mocked_movie_id, API_KEY)
  assert isinstance(retval, dict)
