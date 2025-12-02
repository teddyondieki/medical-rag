from dotenv import load_dotenv
import os

load_dotenv()

HF_TOKEN = os.environ.get("HF_TOKEN")
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
HUGGINGFACE_REPO_ID = os.environ.get("HUGGINGFACE_REPO_ID", "Qwen/Qwen2.5-7B-Instruct")
DB_FAISS_PATH = os.environ.get("DB_FAISS_PATH", "vectorstore/db_faiss")
DATA_PATH = os.environ.get("DATA_PATH", "data/")
CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 500))
CHUNK_OVERLAP = int(os.environ.get("CHUNK_OVERLAP", 50))

# Flask configuration
DEBUG = True
