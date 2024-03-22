from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def transformStringToVector(text):
    return model.encode(text)