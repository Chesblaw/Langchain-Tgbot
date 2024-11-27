from langchain_cohere import ChatCohere, CohereEmbeddings
from langchain_chroma import Chroma
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from create_database import generate_data_store
from dotenv import load_dotenv
import os

# Load variables from .env file
generate_data_store()
load_dotenv()
CHROMA_PATH = "./chroma_db"
COHERE_API_KEY = os.getenv("COHERE_API_KEY")

# Initialize large language model and embedding model
model = ChatCohere(model="command-r-plus", cohere_api_key=COHERE_API_KEY)
embedding_function = CohereEmbeddings(model="embed-english-v3.0")

# Initialize vector store 
vectorstore = Chroma(embedding_function=embedding_function,persist_directory = CHROMA_PATH)
retriever = vectorstore.as_retriever()

system_prompt = (
    "You are an assistant designed to assist users by providing information, if possible based on the context provided."
    "You must not guess, provide information that is not explicitly mentioned, hallucinate or create answers ."
    "Keep it concise."
    "\n\n"
    "{context}"
)
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)

chain = (
    {'context': retriever, 'input': RunnablePassthrough()}
    | prompt
    | model
    | StrOutputParser()
)

def process_message(query):
    response = chain.invoke(query)
    return response
