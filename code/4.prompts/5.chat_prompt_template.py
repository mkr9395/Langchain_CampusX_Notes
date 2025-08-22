# using chat_prompt_template for list of meassages sending dynamically

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI()

# system and human message will be send as a tuple
chat_template = ChatPromptTemplate([
    ('system','You are a helpful {domain} expert'),
    ('human', 'Explain in simple terms what is {topic}')
    ])

prompt = chat_template.invoke({'domain': 'cricket', 'topic': 'reverse swing'})

print(prompt)
