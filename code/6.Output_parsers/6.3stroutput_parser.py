# now implementing the same with stroutputparser

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import PromptTemplate

load_dotenv()

model = ChatOpenAI()

# 1st prompt -> detailed report

template1 = PromptTemplate(
    template = 'Write a detailed report on {topic}',
    input_variables= ['topic'])


# 2nd prompt -> summary
template2 = PromptTemplate(
    template = 'Write a 5 line summary on the following text \n {text}',
    input_variables= ['text'])

prompt1 = template1.invoke({'topic':'Blackhole'})


# string ouput parser
parser = StrOutputParser() # will give detailed report

# forming a chain

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic':'Blackhole'})

print(result)