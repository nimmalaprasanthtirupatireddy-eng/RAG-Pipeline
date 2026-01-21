# RAG-Pipeline

# 📄 Retrieval-Augmented Generation (RAG) Application  
### (Powered by Ollama – Gemma2:2B)

This project implements a **Retrieval-Augmented Generation (RAG)** system using a **locally running LLM (Gemma2:2B via Ollama)**.  
It combines **document retrieval** with **context-aware generation** to answer user queries accurately — without relying on cloud-based APIs.

---

## 🚀 Features

- 📚 Document ingestion and text chunking
- 🔍 Semantic search using vector embeddings
- 🤖 Local LLM inference using **Ollama (Gemma2:2B)**
- ⚡ FastAPI backend for RAG APIs
- 🖥️ Streamlit frontend for user interaction
- 🔗 LangChain for RAG pipeline orchestration
- 🔐 Fully local & offline-friendly setup

---

## 🛠️ Tech Stack

- **Language:** Python  
- **Backend:** FastAPI  
- **Frontend:** Streamlit  
- **LLM Framework:** LangChain  
- **LLM:** Ollama – `gemma2:2b`  
- **Vector Store:** FAISS / Chroma  
- **Embeddings:** Ollama / HuggingFace  

---

## 📂 Project Structure

RAG-Pipeline/

│

├── api.py

├── main.py

├── app.py

├── requirements.txt


---

## ⚙️ Prerequisites

### 1️⃣ Install Ollama
Download and install Ollama from:

https://ollama.com


Verify installation:
```bash
ollama --version

ollama pull gemma2:2b

ollama run gemma2:2b
```

⚙️ Installation

1️⃣ Clone the repository

git clone https://github.com/nimmalaprasanthtirupatireddy-eng/RAG-Pipeline.git
cd RAG-Pipeline

2️⃣ Create virtual environment

```bash
python -m venv venv

venv\Scripts\activate       
```

3️⃣ Install dependencies

``` bash
pip install -r requirements.txt
```

▶️ How to Run the Application

1️⃣ Start Ollama server

Ollama usually runs automatically. If needed:

ollama serve

2️⃣ Start FastAPI Backend
```bash
uvicorn api:app --reload
```
http://127.0.0.1:8000

3️⃣ Start Streamlit Frontend

Open a new terminal:
```bash
streamlit run app.py
```
http://localhost:8501



🧠 RAG Pipeline Flow

Load documents from /data/documents

Split text into chunks

Generate embeddings

Store embeddings in vector database

Retrieve top-k relevant chunks

Pass context + query to Gemma2:2B

Generate grounded response


📌 Advantages of Using Ollama + Gemma2

✅ Fully local execution

✅ No API cost

✅ Better data privacy

✅ Works offline

✅ Ideal for personal & enterprise RAG systems


📌 Future Enhancements

📄 Upload PDFs from UI

🗄️ Persistent vector DB

🔄 Multi-model switching

🔐 User authentication

📊 Query analytics

🤝 Contributing


Contributions are welcome!

Fork the repository and submit a pull request.


⭐ Acknowledgements

Ollama

Google Gemma

LangChain

FastAPI

Streamlit


Created by & Contact 

Name : Nimmala Prasanth Tirupati Reddy

email : nimmalaprasanthtirupatireddy@gmail.com

github : https://github.com/nimmalaprasanthtirupatireddy-eng

