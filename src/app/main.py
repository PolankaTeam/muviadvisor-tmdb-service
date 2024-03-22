from services.tmdb import *
from routers import movies
import uvicorn
from fastapi import Depends, FastAPI

app = FastAPI()

app.include_router(movies.router)


import requests
import json
from sentence_transformers import SentenceTransformer
import chromadb

model = SentenceTransformer('all-MiniLM-L6-v2')

resp = requests.get('https://raw.githubusercontent.com/weaviate-tutorials/quickstart/main/data/jeopardy_tiny.json')
data = json.loads(resp.text)  # Load data

documents = []
metadatas = []
embeddings = []
ids = []

for index, data in enumerate(data):
    documents.append(data.get("Question", ""))
    embedding = model.encode(data['Question']).tolist()
    embeddings.append(embedding)
    metadatas.append({'category': data['Category'], 'answer': data['Answer']})
    ids.append(str(index + 1))

client = chromadb.HttpClient(host='localhost', port=8000)
collection = client.get_collection('my-questions')

collection.add(
    documents=documents,
    embeddings=embeddings,
    metadatas=metadatas,
    ids=ids
)

query = "dog"
input_em = model.encode(query).tolist()

results = collection.query(
    query_embeddings=[input_em],
    n_results=3
)

results = json.dumps(results)
results = json.loads(results)
print(results)

gowno = {'title': 'gówno jebane'}

@app.get("/")
async def root():
    return results


    
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=3500, reload=True)










