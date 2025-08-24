# load from web pages which are static

from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI()

prompt = PromptTemplate(
    template='Answer the following question \n {question} from the following text - \n {text}',
    input_variable = ['question', 'text']    
    
)

parser = StrOutputParser()

url ="https://towardsdatascience.com/is-googles-reveal-of-geminis-impact-progress-or-greenwashing/"

loader = WebBaseLoader(url)

docs = loader.load()

chain = prompt | model | parser

print(chain.invoke({'question':'What is the prodcut that we are talking about?', 'text':docs[0].page_content}))

# print(len(docs))

# print(docs[0].page_content)





