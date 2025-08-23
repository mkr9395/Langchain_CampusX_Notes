# TinyLlama/TinyLlama-1.1B-Chat-v1.0 is not working

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate

load_dotenv()

llm = HuggingFaceEndpoint(
    # repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)


# 1st prompt -> detailed report

template1 = PromptTemplate(
    template = 'Write a detailed report on {topic}',
    input_variables= ['topic'])


# 2nd prompt -> summary
template2 = PromptTemplate(
    template = 'Write a 5 line summary on the following text \n {text}',
    input_variables= ['text'])

prompt1 = template1.invoke({'topic':'Blackhole'})

result = model.invoke(prompt1)

prompt2 = template2.invoke({'text': result.content})

final_result = model.invoke(prompt2)

print(final_result.content)