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


import logging
from PyPDF2 import PdfReader 
from langchain.text_splitter import RecursiveCharacterTextSplitter 
from langchain_huggingface import HuggingFaceEmbeddings 
from langchain_core.runnables import RunnablePassthrough
from langchain.llms import Ollama 
from langchain.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)
logger = logging.getLogger(__name__)


class SimpleRAG: 
    def __init__(self): 
        logger.info("Initializing SimpleRAG")
        self.embeddings = HuggingFaceEmbeddings( 
            model_name="sentence-transformers/all-MiniLM-L6-v2"
            ) 
        self.llm = Ollama(model="gemma2:2b") 
        self.vector_db = None 
        self.prompt = PromptTemplate(
            template="""
            Your an Helpful Assistant
            Use the following context to answer the question.
            If the answer is not in the context, say "I don't know".
            
            Content:
            {content}

            Question:
            {question}

            Answer:
            """,
            input_variables=["content","question"]
        )
        self.parser = StrOutputParser()
        logger.info("SimpleRAG initialized successfully")
    
    def read_text(self, pdf_path): 
        logger.info(f"Reading PDF:{pdf_path}")
        reader = PdfReader(pdf_path) 
        text = "" 
        
        for i,page in enumerate(reader.pages): 
            page_text = page.extract_text() 
            
            if page_text: 
                text += page_text + "\n" 
            logger.debug(f"Processed page {i+1}")
        logger.info(f"Finished reading PDF ({len(reader.pages)} pages)")
        return text 
    
    def chunk_text(self, text): 
        logger.info("Splitting text into chunks")
        splitter = RecursiveCharacterTextSplitter( chunk_size=500, chunk_overlap=100 )
        chunks = splitter.split_text(text) 
        logger.info(f"Created {len(chunks)}")
        return chunks 
    
    def store_in_vector_db(self, chunks): 
        logger.info("Storing chunks in vector database")
        if self.vector_db is None:
            self.vector_db = FAISS.from_texts(chunks, self.embeddings) 
            logger.info("Vector DB created")
        else:
            self.vector_db.add_texts(chunks)
            logger.info("Vector DB updated with new chunks")
    
    def ask_question(self, question): 
        logger.info(f"Recived question : {question}")
        if self.vector_db is None: 
            logger.info("Vector DB not intialized")
            raise ValueError("Vector DB not initialized") 
        retriever = self.vector_db.as_retriever()

        docs = retriever.get_relevant_documents(question)
        logger.info(f"Retrived {len(docs)} relevent documnets")

        for i , doc in enumerate(docs):
            logger.info(f"Doc {i+1} : {doc.page_content[:200]}")

        rag_chain = (
            {
                "content":retriever,
                "question":RunnablePassthrough()
            }
            |self.prompt
            |self.llm
            |self.parser
        )

        logger.info("Invoke RAG chain")
        answer = rag_chain.invoke(question)

        logger.info("LLM response generated")
        return answer
