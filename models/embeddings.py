from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os

def get_embedding_model():
    return GoogleGenerativeAIEmbeddings(model='models/embedding-001',google_api_key='your_google_api_key_here')