
from langchain.text_splitter import RecursiveCharacterTextSplitter 


# NEW (Updated)
from langchain_huggingface import HuggingFaceEmbeddings  

# New (Updated)
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter 
 

# Extract Data from the pdf file 

def load_pdf_file(data):
    loader = DirectoryLoader(data,
                             glob = "*.pdf",
                             loader_cls = PyPDFLoader)
    
    documents = loader.load()

    return documents



# split the data  into text chunks 

def text_split(extracted_data) :
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 20 )
    text_chunks = text_splitter.split_documents(extracted_data)

    return text_chunks



def download_hugging_face_embeddings():
    # NEW (Updated)
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    return embeddings

embeddings = download_hugging_face_embeddings()


