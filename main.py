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
