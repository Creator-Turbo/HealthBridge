from langchain.prompts import ChatPromptTemplate





system_prompt = (" You are an assistant for question-answering tasks. "
"Use the following pieces of retrieved context to answer the question. "
"If you don't know the answer, just say that you don't know. "
"Use ten sentences maximum and keep the answer concise. " 
"answer concise"
"\n\n"
"{context}"
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human","{input}"),
    ]
)

