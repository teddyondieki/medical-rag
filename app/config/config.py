import os
HF_TOKEN = os.environ.get("HF_TOKEN")

# Flask configuration
DEBUG = True

HUGGINGFACE_REPO_ID="google/flan-t5-base"
DB_FAISS_PATH="vectorstore/db_faiss"
DATA_PATH="data/"
CHUNK_SIZE=500
CHUNK_OVERLAP=50
