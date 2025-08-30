# now doing with OPENAI as TinyLLAMA is not working

# This is without implementing StrOutputParser -> very long code where you have to invoke twice


from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
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

result = model.invoke(prompt1)

prompt2 = template2.invoke({'text': result.content})

final_result = model.invoke(prompt2)

print(final_result.content)