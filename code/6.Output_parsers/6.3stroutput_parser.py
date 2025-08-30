# now implementing the same with StrOutputParser -> helps in building chain for multiple models in the chain

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


# string ouput parser
parser = StrOutputParser() # will give detailed report

# forming a chain (was able to build chain bcoz of stroutputparser)

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic':'Blackhole'}) # directly run the topic here

print(result)