from fastapi import FastAPI,HTTPException, Body
from pydantic import BaseModel
from models.embeddings import get_embedding_model
from database.chroma import get_chroma_client,create_or_load_index,upsert_documents
from services.google_gemini import get_google_customsearch_service
from typing import List
import os
from dotenv import load_dotenv
load_dotenv('API_KEY.env')
GOOGLE_API_KEY = os.getenv('GOOGLE_KEY')
os.environ['GOOGLE_API_KEY'] = GOOGLE_API_KEY

app = FastAPI()

embedding_model = get_embedding_model()
chroma_index = create_or_load_index()
google_customsearch_service = get_google_customsearch_service(GOOGLE_API_KEY)

class Document(BaseModel):
    id:str
    content:str

class Query(BaseModel):
    question:str

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}

@app.post('/upsert-documents/')
def upsert_docs(docs:List[Document]):
    upsert_documents(chroma_index,docs)
    return{'status':'ok'}


@app.post("/query/")
def query_docs(query: Query):
    print(f"Received query: {query.question}")
    embedding_input = query.question
    print(f"Embedding input type: {type(embedding_input)}, value: {embedding_input}")
    embedding = embedding_model.embed_query(embedding_input)  # Ensure this is a string
    print(f"Embedding result type: {type(embedding)}, value: {embedding}")
    results = chroma_index.similarity_search_by_vector(embedding)
    return {"results": results}
