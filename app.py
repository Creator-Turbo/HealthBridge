from flask import Flask, render_template, request, jsonify
from src.helper import download_hugging_face_embeddings
# from langchain_pinecone import PineconeVector
from langchain_community.vectorstores import Pinecone as p 
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

docsearch = p.from_existing_index(
    index_name = index_name,
    embedding = embeddings
)


retriever = docsearch.as_retriever(search_type = "similarity",search_kwargs ={"k":3})




llm = HuggingFaceHub(
    huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN,
    # repo_id="mistralai/Mistral-7B-Instruct-v0.3",
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


# from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
# from flask_mail import Mail, Message
# from pymongo import MongoClient
# import uuid
# import os
# from dotenv import load_dotenv
# from src.helper import download_hugging_face_embeddings
# from langchain_pinecone import PineconeVectorStore
# from langchain_community.llms import HuggingFaceHub
# from langchain.chains import create_retrieval_chain
# from langchain.chains.combine_documents import create_stuff_documents_chain
# from langchain_core.prompts import ChatPromptTemplate
# from src.prompt import *

# # App setup
# app = Flask(__name__)
# app.secret_key = "supersecretkey"
# load_dotenv()

# # Email Config
# app.config['MAIL_SERVER'] = 'smtp.gmail.com'
# app.config['MAIL_PORT'] = 587
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USERNAME'] = os.getenv("EMAIL_USER")
# app.config['MAIL_PASSWORD'] = os.getenv("EMAIL_PASS")
# mail = Mail(app)

# # MongoDB Setup
# client = MongoClient(os.getenv("MONGODB_URI"))
# db = client['medicalbot_db']
# users_collection = db['users']
# appointments_collection = db['appointments']

# # API Keys
# PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
# HUGGINGFACEHUB_API_TOKEN = os.getenv('HUGGINGFACEHUB_API_TOKEN')
# os.environ['PINECONE_API_KEY'] = PINECONE_API_KEY
# os.environ['HUGGINGFACEHUB_API_TOKEN'] = HUGGINGFACEHUB_API_TOKEN

# # Langchain Setup
# embeddings = download_hugging_face_embeddings()
# docsearch = PineconeVectorStore.from_existing_index(index_name="medicalbot", embedding=embeddings)
# retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k": 3})

# llm = HuggingFaceHub(
#     huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN,
#     repo_id="mistralai/Mistral-7B-Instruct-v0.3",
#     model_kwargs={"temperature": 1, "max_length": 180}
# )

# prompt = ChatPromptTemplate.from_messages([
#     ("system", system_prompt),
#     ("human", "{input}"),
# ])
# question_answer_chain = create_stuff_documents_chain(llm, prompt)
# rag_chain = create_retrieval_chain(retriever, question_answer_chain)

# # Routes
# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/sign-up", methods=['GET', 'POST'])
# def signup():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         if users_collection.find_one({"username": username}):
#             flash("Username already exists!", "danger")
#             return redirect(url_for('signup'))
#         users_collection.insert_one({"username": username, "password": password})
#         flash("Signup successful! Please login.", "success")
#         return redirect(url_for('login'))
#     return render_template("signup.html")

# @app.route("/", methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         user = users_collection.find_one({"username": username, "password": password})
#         if user:
#             session['username'] = username
#             flash("Login successful!", "success")
#             return redirect(url_for('dashboard'))
#         flash("Invalid credentials!", "danger")
#     return render_template("login.html")

# @app.route("/logout")
# def logout():
#     session.pop('username', None)
#     flash("Logged out successfully.", "info")
#     return redirect(url_for('login'))

# @app.route("/dashboard")
# def dashboard():
#     if 'username' not in session:
#         return redirect(url_for('login'))
#     return render_template("dashboard.html")

# @app.route("/appoinment", methods=['GET', 'POST'])
# def schedule():
#     if 'username' not in session:
#         return redirect(url_for('login'))
#     if request.method == 'POST':
#         email = request.form['email']
#         date = request.form['date']
#         zoom_link = f"https://zoomclone.com/meeting/{uuid.uuid4()}"
#         appointments_collection.insert_one({
#             "username": session['username'],
#             "email": email,
#             "date": date,
#             "zoom_link": zoom_link
#         })

#         msg = Message('Appointment Confirmation', sender=app.config['MAIL_USERNAME'], recipients=[email])
#         msg.body = f"Hello, your appointment is scheduled for {date}. Join here: {zoom_link}"
#         mail.send(msg)

#         flash("Appointment scheduled and email sent!", "success")
#         return redirect(url_for('dashboard'))
#     return render_template("schedule.html")

# @app.route("/get", methods=["POST"])
# def chat():
#     msg = request.form["msg"]
#     response = rag_chain.invoke({"input": msg})
#     return str(response["answer"])

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000, debug=True)