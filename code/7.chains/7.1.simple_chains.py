from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(
    template = 'Write 5 intersting facts on {topic}',
    input_variables= ['topic']
    
)

# need parser that give string output
parser = StrOutputParser()

# forming a chain

chain = prompt | model | parser

result = chain.invoke({'topic':'Cricket'})

print(result)

# to view steps in the chain
chain.get_graph().print_ascii()