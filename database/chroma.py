from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

def get_chroma_client():
    pass

def create_or_load_index(index_name='knowledge_base'):
    embeddings = GoogleGenerativeAIEmbeddings(model='models/embedding-001', google_api_key='AIzaSyAmlzXyisknetIo4DRWo97e9pQqAQuuCvQ')
    return Chroma(embedding_function=embeddings)

def upsert_documents(chroma_index, docs):
    texts = [doc.content for doc in docs]
    metadatas = [{'id': doc.id} for doc in docs]
    chroma_index.add_texts(texts, metadatas)



