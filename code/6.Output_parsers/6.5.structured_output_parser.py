# using structureoutputparse to get the desired structure of output

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

from langchain.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

llm = HuggingFaceEndpoint(
    # repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

# the schema which we want
schema = [
    ResponseSchema(name= 'fact_1', description = 'Fact 1 about the topic'),
    ResponseSchema(name= 'fact_2', description = 'Fact 2 about the topic'),
    ResponseSchema(name= 'fact_3', description = 'Fact 3 about the topic')
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template = 'Give 3 facts about the {topic} \n {format_instruction}',
    input_variables = ['topic'],
    partial_variables = {'format_instruction': parser.get_format_instructions()}
    )
    
# without chains  
# prompt = template.invoke({'topic':'Blackhole'})

# result = model.invoke(prompt)

# final_result = parser.parse(result.content)

# print(final_result)

# print(type(final_result))


# doing same with chains
chain = template | model | parser
result = chain.invoke({'topic':'Blackhole'}) # if no input variable then send blank dictionary


print(result)
print(type(result))

