from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough, RunnableSequence, RunnableParallel, RunnableLambda, RunnableBranch
from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate(
    template = 'Give me detailed report about the character {name} with less than 100 words',
    input_variables= ['name']
)

prompt2 = PromptTemplate(
    template = 'Give me a summary of the following text \n {text} in atmost 30 words',
    input_variables= ['text']
)

model = ChatOpenAI()
parser = StrOutputParser()

# genearitng report about the charcter
# report_gen_chain = RunnableSequence(prompt1, model, parser)
report_gen_chain = prompt1 | model | parser # another way of performing runnablesequence



# RunnableBranch takes tuple for each condition and at end default condition
branch_chain = RunnableBranch(
    (lambda x : len(x.split()) > 50, RunnableSequence(prompt2, model, parser)), # if more than 50 words then summary in 30 words
    RunnablePassthrough() # else pass the report as it is less than 50 words then do nothing
)

final_chain = RunnableSequence(report_gen_chain, branch_chain)

result = final_chain.invoke({'name':'Harry Potter'})

print(result)

final_chain.get_graph().print_ascii()