from flask import Flask, render_template, request, jsonify
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
# from langchain import HuggingFaceHub
from langchain_community.llms import HuggingFaceHub
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

from dotenv import load_dotenv
from src.prompt import *
import os 



app = Flask(__name__)
load_dotenv()

# PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
# HUGGINGFACEHUB_API_TOKEN = os.environ.get('HUGGINGFACEHUB_API_TOKEN')

# # Store them in environment variables
# load_dotenv()
# os.environ['PINECONE_API_KEY'] = PINECONE_API_KEY
# os.environ['HUGGINGFACEHUB_API_TOKEN'] = HUGGINGFACEHUB_API_TOKEN

# Load environment variables from .env file
load_dotenv()

# Get API keys from environment variables
PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
HUGGINGFACEHUB_API_TOKEN = os.getenv('HUGGINGFACEHUB_API_TOKEN')

# Validate if the keys are loaded correctly
if not PINECONE_API_KEY:
    raise ValueError("Error: PINECONE_API_KEY is not set. Check your .env file.")
if not HUGGINGFACEHUB_API_TOKEN:
    raise ValueError("Error: HUGGINGFACEHUB_API_TOKEN is not set. Check your .env file.")

# Store them explicitly in environment variables
os.environ['PINECONE_API_KEY'] = PINECONE_API_KEY
os.environ['HUGGINGFACEHUB_API_TOKEN'] = HUGGINGFACEHUB_API_TOKEN

print("API keys loaded successfully!")


embeddings = download_hugging_face_embeddings()




index_name = "medicalbot"

# Embed each chunk and upsert the embeddings into your Pinecone index 

docsearch = PineconeVectorStore.from_existing_index(
    index_name = index_name,
    embedding = embeddings
)


retriever = docsearch.as_retriever(search_type = "similarity",search_kwargs ={"k":3})




llm = HuggingFaceHub(
    huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN,
    repo_id="mistralai/Mistral-7B-Instruct-v0.3",
    model_kwargs={"temperature": 1, "max_length": 180}
)




prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human","{input}"),
    ]
)

question_answer_chain = create_stuff_documents_chain(llm, prompt)

rag_chain = create_retrieval_chain(retriever, question_answer_chain)



@app.route("/")
def index():
    return render_template('index.html') 



@app.route("/get", methods=["GET", "POST"])

def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    response = rag_chain.invoke({"input":msg})
    print("Response :",response["answer"])

    return str(response["answer"])



if __name__ == "__main__":
     app.run(host="0.0.0.0", port=5000
             , debug=True)


