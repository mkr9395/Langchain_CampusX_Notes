# genearting multiple embeddings

from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model = "text-embedding-3-small", dimensions=32)

document = [
    "Delhi is capital of India",
    "Mumbai is the financial capital of India",
    "Bangalore is the IT hub of India"
]

# change to embed_documents to generate for documents
result = embedding.embed_documents(document)

print(str(result))
print(len(result))
