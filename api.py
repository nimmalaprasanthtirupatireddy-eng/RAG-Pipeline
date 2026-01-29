from fastapi import FastAPI, UploadFile, File 
import shutil 
import os 
from main import SimpleRAG 

app = FastAPI(title="Simple RAG API") 

rag = SimpleRAG() 

UPLOAD_DIR = "uploads" 
os.makedirs(UPLOAD_DIR, exist_ok=True) 

@app.post("/upload-pdf/") 
async def upload_pdf(file: UploadFile = File(...)): 
    file_path = os.path.join(UPLOAD_DIR, file.filename) 
    
    with open(file_path, "wb") as buffer: 
        shutil.copyfileobj(file.file, buffer) 
        text =await rag.read_text(file_path) 
        chunks =await rag.chunk_text(text) 
        await rag.store_in_vector_db(chunks) 
    return {"message": "PDF processed and stored successfully"} 

@app.post("/ask/") 
async def ask_question(question: str): 
    answer = await rag.ask_question(question) 
    return {"answer": answer}