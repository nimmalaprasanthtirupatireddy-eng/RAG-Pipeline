from langchain.vectorstores import FAISS
from .logger import logger

def create_or_update_vector_db(chunks, embeddings, vector_db=None):
    if vector_db is None:
        logger.info("Creating new Vector DB")
        return FAISS.from_texts(chunks, embeddings)

    logger.info("Updating Vector DB with new chunks")
    vector_db.add_texts(chunks)
    return vector_db
