import chromadb
from services.sentence_transformer import transformStringToVector
import json

class ChromaDbClient:

    def __init__(self, host, port):
        self.host = host
        self.port = port 
        self.client = chromadb.HttpClient(host=self.host, port= self.port)

    def __init__(self):
        self.client = chromadb.HttpClient(host='localhost', port=8000)

    def populateColletionWithDataFromTMDB(self, collectionName: str, tmdbData: dict):
        documents = []
        metadatas = []
        embeddings = []
        ids = []

        for movie in tmdbData:
            documents.append(movie.get("overview", ""))
            embedding = transformStringToVector(movie.get("overview", "")).tolist()
            embeddings.append(embedding)
            metadatas.append({
                "adult": str(movie.get("adult", "")),
                "original_language": movie.get("original_language", ""),
                "original_title": movie.get("original_title", ""),
                "popularity": str(movie.get("popularity", "")),
                "release_date": movie.get("release_date", ""),
                "title": movie.get("title", ""),
                "vote_average": str(movie.get("Question", "")),
            })
            ids.append(str(movie.get("id", "")))

        try:
            self.client.get_collection(collectionName)
        except Exception as e:
            self.client.create_collection(collectionName)

        collection = self.client.get_collection(collectionName)
    
        collection.add(
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas,
            ids=ids
        )

        return "Data populated"

    def semanticSearchCollection(self, query: str, collectionName: str, numberOfResults: int):
        vectorizedQuery = transformStringToVector(query).tolist()
        collection = self.client.get_collection(collectionName)
        results = collection.query(
            query_embeddings=[vectorizedQuery],
            n_results=numberOfResults
        )
        results = json.dumps(results)
        results = json.loads(results)

        return results
    
    def createNewCollection(self, collectionName):
        self.client.create_collection(collectionName)

        
