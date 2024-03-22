from fastapi import APIRouter, Depends, HTTPException
from services.tmdb import *
from services.chromadbClient import ChromaDbClient

router = APIRouter()

#######-------EXAMPLE--------------#############
# fake_items_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}

# @router.get("/{item_id}")
# async def read_item(item_id: str):
#     if item_id not in fake_items_db:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return {"name": fake_items_db[item_id]["name"], "item_id": item_id}
#########-------------------------------##################

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


