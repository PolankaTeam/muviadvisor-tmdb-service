from services.tmdb import *
from routers import movies
from routers import chromaDbAPI
import uvicorn
from fastapi import Depends, FastAPI

app = FastAPI()

app.include_router(movies.router)
app.include_router(chromaDbAPI.router)

@app.get("/")
async def root():
    return "Welcome to Muviadvisor! :)"

    
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=3500, reload=True)










