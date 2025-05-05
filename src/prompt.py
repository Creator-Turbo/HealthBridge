from langchain.prompts import ChatPromptTemplate





# system_prompt = (" You are an assistant for question-answering tasks. "
# "Use the following pieces of retrieved context to answer the question. "
# "If you don't know the answer, just say that you don't know. "
# "Use ten sentences maximum and keep the answer concise. " 
# "answer concise"
# "\n\n"
# "{context}"
# )

# prompt = ChatPromptTemplate.from_messages(
#     [
#         ("system", system_prompt),
#         ("human","{input}"),
#     ]
# )

from langchain.prompts import ChatPromptTemplate

system_prompt = (
    "You are a helpful assistant specialized in medical Q&A.\n"
    "Use the following context to extract only the treatment advice "
    "for someone who has a fever.\n"
    "If treatment is not mentioned, say 'Treatment not found in the context.'\n"
    "Answer in a single paragraph.\n\n"
    "{context}"
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "Extract only the treatment advice for fever from the above context."),
    ]
)

