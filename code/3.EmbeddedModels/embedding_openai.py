# single query embedding using OpenAI's text-embedding-3-small model

from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model = "text-embedding-3-small", dimensions=32)

result = embedding.embed_query("Delhi is capital of India")

print(str(result))
print(len(result))



# from openai import OpenAI
# client = OpenAI()

# response = client.embeddings.create(
#     input="Your text string goes here",
#     model="text-embedding-3-small"
# )

# print(response.data[0].embedding)