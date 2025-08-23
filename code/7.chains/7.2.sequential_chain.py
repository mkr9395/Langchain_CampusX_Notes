# 2 LLMs call
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv  

load_dotenv()

prompt1 = PromptTemplate(
    template = 'Write a detailed report on {topic}',
    input_variables= ['topic'])

prompt2 = PromptTemplate(
    template = 'Write a 5 line summary on the following text \n {text}',
    input_variables= ['text'])

model = ChatOpenAI()

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({'topic':'jobs in Gen ai field in India'})

print(result)

# to view steps in the chain
chain.get_graph().print_ascii()

