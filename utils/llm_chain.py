from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

def build_llm_chain(llm, retriever):
    prompt = PromptTemplate(
        template="""
            You are a document-based assistant.

            Task:
            Answer the user's question using ONLY the provided context.

            Content:
            {content}

            Question:
            {question}

            Strict Rules (follow in order):

            Step 1:
            Check whether the context contains enough information
            to answer the question.

            - If NO, respond exactly:
            "The answer is not available in the provided documents."
            - STOP immediately.

            Step 2:
            If YES, identify the question type answer with sutable one answer type:
            - Definition (what is / meaning)
            - Steps or Process (how / steps / procedure)
            - Concept or Explanation (why / concept / theory)

            Step 3:
            Format the answer accordingly:
            - Definition → ONE clear paragraph
            - Steps/Process → Numbered points
            - Concept → Explanation WITH a simple example

            Additional Rules:
            - Use ONLY the given context
            - Do NOT add external knowledge
            - Do NOT guess or infer""",
            input_variables=["content","question"]
        )
    parser = StrOutputParser()

    rag_chain = (
        {
            "content": retriever,
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
        | parser
    )

    return rag_chain
