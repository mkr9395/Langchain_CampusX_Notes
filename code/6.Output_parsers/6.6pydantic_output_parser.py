# using pydantic
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate

from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from dotenv import load_dotenv  

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
    )

model = ChatHuggingFace(llm=llm)


class Person(BaseModel):
    name :str = Field(description='name of the person')
    age : int = Field(gt=18, description='age of the person') # adding constriant = age should be greater than 18
    city : str = Field(description='name of the city the person belongs to')
    
# parser which will be PydanticOutputParser used to parse the output in the form of Pydantic model    
parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template = 'Give me the name, age, city of a fictional {place} person \n {format_instruction}',
    input_variables = ['place'],
    partial_variables = {'format_instruction': parser.get_format_instructions()}
)

# without chains

# prompt = template.invoke({'place':'india'})

# result = model.invoke(prompt)

# final_result = parser.parse(result.content)

# print(final_result)



# with chains
chain = template | model | parser

final_result = chain.invoke({'place':'russia'})

print(final_result)
