from langchain_community.document_loaders import TextLoader
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(
    template = 'Write a summary for the following poem \n {poem}',
    input_variables= ['poem']
    )
parser = StrOutputParser()



loader = TextLoader("cricket.txt",encoding='utf8')

docs = loader.load()

print(docs)

print(type(docs))

print(len(docs))

print(docs[0])

print("docs page content : ",docs[0].page_content)

print("docs metadata : ",docs[0].metadata)

# creating chain :
chain = prompt | model | parser

# page content will go as input
result = chain.invoke({'poem':docs[0].page_content})

print(result)