# Store documents as Pinecone vector embedding

from src.helper import load_pdf_file, text_split, download_hugging_face_embeddings
from pinecone.grpc import PineconeGRPC as pinecone
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os

load_dotenv()

PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

extracted_data = load_pdf_file("data/")
text_chunks = text_split(extracted_data)
embeddings = download_hugging_face_embeddings()

# Pinecone initialization
pc = Pinecone(api_key = os.environ.get("PINECONE_API_KEY"))
index_name = "genai-medical-bot"

if not pc.has_index(index_name):
    pc.create_index_for_model(
        name=index_name,
        cloud="aws",
        region="us-east-1",
        embed={
            "dimension": 384,
            "model":"llama-text-embed-v2",
            "field_map":{"text": "chunk_text"},
            "metric": "cosine"
        }
    )

    print(f"Index {index_name} created successfully !!")

else:
    print(f"Index {index_name} already exists.")