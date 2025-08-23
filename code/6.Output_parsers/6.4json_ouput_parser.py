from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    # repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()

template = PromptTemplate(
    template = 'Give me the name, age, city of a fictional character \n {format_instruction}',
    input_variables = [],
    partial_variables = {'format_instruction': parser.get_format_instructions()})
    
    
# prompt = template.format()

# result = model.invoke(prompt)

# final_result = parser.parse(result.content)

# print(final_result)
# print(final_result['name'])
# print(type(final_result))


# doing same with chains
chain = template | model | parser
result = chain.invoke({}) # if no input variable then send blank dictionary


print(result)
print(result['name'])
print(type(result))

