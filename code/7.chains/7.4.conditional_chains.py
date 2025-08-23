# if positive feedback then 1 response if negative then the other
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser

from pydantic import BaseModel, Field
from typing import Literal

from dotenv import load_dotenv


load_dotenv()

model = ChatOpenAI()

parser = StrOutputParser()

# structuing the output to get what we want
class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field('give the sentiment of the feedback')

parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template = 'Classify the following feedback text as positive or negative \n {feedback} \n {format_instruction}',
    input_variables= ['feedback'],
    partial_variables = {'format_instruction': parser2.get_format_instructions()}
    )

classifier_chain = prompt1 | model | parser2

# for pos feedback
prompt2 = PromptTemplate(
    template = 'Write an appropriate response to the following positive feedback \n {feedback}',
    input_variables= ['feedback']
    )

# for neg feedback
prompt3 = PromptTemplate(
    template = 'Write an appropriate response to the following negative feedback \n {feedback}',
    input_variables= ['feedback']
    )

branch_chain = RunnableBranch(
    (lambda x : x.sentiment == 'positive', prompt2 | model | parser), # (condition1, chain1) -> condition, what excutes if condition is true
    (lambda x : x.sentiment == 'negative', prompt3 | model | parser),
    RunnableLambda(lambda x : "could not find sentiment") # default chain which should be runnable
)
    
    
    
chain = classifier_chain | branch_chain

print(chain.invoke({'feedback':'The product is really good and I am not satisfied with the quality'}))

chain.get_graph().print_ascii()
    