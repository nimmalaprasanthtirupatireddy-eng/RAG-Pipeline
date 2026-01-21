# from PyPDF2 import PdfReader
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.embeddings import HuggingFaceEmbeddings
# from langchain.chains import RetrievalQA
# from langchain.llms import Ollama 
# from langchain.vectorstores import FAISS

# class simpleRAG:
#     def __init__(self):
#         self.embeddings = HuggingFaceEmbeddings(
#             model = 'sentence-transformers/all-MiniLM-L6-v2'
#         )
#         self.llm = Ollama(model='gemma2:2b')
#         self.vector_db=None

#     def read_text(self,pdf_path):
#         reader = PdfReader(pdf_path)
#         text = ''

#         for page in reader.pages:
#             page_text = page.extract_text()
#             if page_text:
#                 text+=page_text+'\n'
#         return text
    
#     def chunk_text(self,text):
#         splitter = RecursiveCharacterTextSplitter(
#             chunk_size=100,
#             chunk_overlap=50
#         )
#         return splitter.split_text(text)
    
#     def store_in_vector_db(self,chunks):
#         self.vector_db = FAISS.from_texts(chunks,self.embeddings)

#     def ask_question(self,question):
#         qa_chain = RetrievalQA.from_chain_type(
#             llm = self.llm,
#             retriever = self.vector_db.as_retriever()
#         )
#         return qa_chain.run(question)
    
# rag = simpleRAG()

# text = rag.read_text("C:\\Users\\nimma\\OneDrive\\Desktop\\Dr. Deepti Chopra - Applied Natural Language Processing with PyTorch 2.0 (2025, Orange Education Pvt L.pdf")

# chunk = rag.chunk_text(text)

# rag.store_in_vector_db(chunk)

# answer = rag.ask_question('What is stemming')

# print(answer)


# from PyPDF2 import PdfReader
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.embeddings import HuggingFaceEmbeddings
# from langchain.chains import RetrievalQA
# from langchain.llms import Ollama
# from langchain.vectorstores import FAISS

# class SimpleRAG:
#     def __init__(self):
#         self.embeddings = HuggingFaceEmbeddings(
#             model_name="sentence-transformers/all-MiniLM-L6-v2"
#         )
#         self.llm = Ollama(model="gemma2:2b")
#         self.vector_db = None

#     def read_text(self, pdf_path):
#         reader = PdfReader(pdf_path)
#         text = ""
#         for page in reader.pages:
#             page_text = page.extract_text()
#             if page_text:
#                 text += page_text + "\n"
#         return text

#     def chunk_text(self, text):
#         splitter = RecursiveCharacterTextSplitter(
#             chunk_size=500,
#             chunk_overlap=100
#         )
#         return splitter.split_text(text)

#     def store_in_vector_db(self, chunks):
#         self.vector_db = FAISS.from_texts(chunks, self.embeddings)

#     def ask_question(self, question):
#         if self.vector_db is None:
#             raise ValueError("Vector DB not initialized")

#         qa_chain = RetrievalQA.from_chain_type(
#             llm=self.llm,
#             retriever=self.vector_db.as_retriever(),
#             return_source_documents=False
#         )

#         return qa_chain.run(question)



# 


# from PyPDF2 import PdfReader
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.embeddings import HuggingFaceEmbeddings
# from langchain.vectorstores import FAISS
# from langchain.chains import RetrievalQA
# from langchain.llms import Ollama
# from langchain.retrievers import BM25Retriever, EnsembleRetriever
# from langchain.schema import Document


# class SimpleRAG:
#     def __init__(self):
#         self.embeddings = HuggingFaceEmbeddings(
#             model_name="sentence-transformers/all-MiniLM-L6-v2"
#         )
#         self.llm = Ollama(model="gemma2:2b")
#         self.text_splitter = RecursiveCharacterTextSplitter(
#             chunk_size=500,
#             chunk_overlap=100
#         )
#         self.documents = []        
#         self.vector_db = None
#         self.bm25_retriever = None
#         self.ensemble_retriever = None
#         self.qa_chain = None

#     def read_text(self, pdf_path):
#         reader = PdfReader(pdf_path)
#         text = ""
#         for page in reader.pages:
#             page_text = page.extract_text()
#             if page_text:
#                 text += page_text + "\n"
#         return text

#     def add_pdf_to_vector_db(self, pdf_path):
#         text = self.read_text(pdf_path)
#         chunks = self.text_splitter.split_text(text)

#         new_docs = [
#             Document(page_content=chunk, metadata={"source": pdf_path})
#             for chunk in chunks
#         ]

#         self.documents.extend(new_docs)

        
#         if self.vector_db is None:
#             self.vector_db = FAISS.from_documents(new_docs, self.embeddings)
#         else:
#             self.vector_db.add_documents(new_docs)

       
#         self.bm25_retriever = BM25Retriever.from_documents(self.documents)
#         self.bm25_retriever.k = 4

        
#         self.ensemble_retriever = EnsembleRetriever(
#             retrievers=[
#                 self.bm25_retriever,
#                 self.vector_db.as_retriever(search_kwargs={"k": 4})
#             ],
#             weights=[0.5, 0.5]
#         )

        
#         if self.qa_chain is None:
#             self.qa_chain = RetrievalQA.from_chain_type(
#                 llm=self.llm,
#                 retriever=self.ensemble_retriever,
#                 return_source_documents=False
#             )

#     def ask_question(self, question):
#         if self.qa_chain is None:
#             raise ValueError("No documents uploaded")

#         return self.qa_chain.run(question)



from PyPDF2 import PdfReader 
from langchain.text_splitter import RecursiveCharacterTextSplitter 
from langchain.embeddings import HuggingFaceEmbeddings 
from langchain.chains import RetrievalQA 
from langchain.llms import Ollama 
from langchain.vectorstores import FAISS

class SimpleRAG: 
    def __init__(self): 
        self.embeddings = HuggingFaceEmbeddings( 
            model_name="sentence-transformers/all-MiniLM-L6-v2"
            ) 
        self.llm = Ollama(model="gemma2:2b") 
        self.vector_db = None 
    
    def read_text(self, pdf_path): 
        reader = PdfReader(pdf_path) 
        text = "" 
        
        for page in reader.pages: 
            page_text = page.extract_text() 
            
            if page_text: 
                text += page_text + "\n" 
        return text 
    
    def chunk_text(self, text): 
        splitter = RecursiveCharacterTextSplitter( chunk_size=500, chunk_overlap=100 ) 
        return splitter.split_text(text) 
    
    def store_in_vector_db(self, chunks): 
        self.vector_db = FAISS.from_texts(chunks, self.embeddings) 
    
    def ask_question(self, question): 
        if self.vector_db is None: 
            raise ValueError("Vector DB not initialized") 
        qa_chain = RetrievalQA.from_chain_type( 
            llm=self.llm, 
            retriever=self.vector_db.as_retriever(), 
            return_source_documents=False 
            ) 
        
        return qa_chain.run(question)
