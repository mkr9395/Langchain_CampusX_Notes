from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv  

from langchain.schema.runnable import RunnableParallel

load_dotenv()

model1 = ChatOpenAI()

model2 = ChatOpenAI(model_name='gpt-3.5-turbo')

prompt1 = PromptTemplate(
    template = 'genearte short and simple notes from the following text \n {text}',
    input_variables= ['text']
    )

prompt2 = PromptTemplate(
    template = 'Generate 3 short question answers from the following text \n {text}',
    input_variables= ['text']
    )

prompt3 = PromptTemplate(
    template = 'merge the provided notes and quiz into a single document \n notes {notes} and quiz {quiz}',
    input_variables= ['notes','quiz']
    )

text = '''After a car wreck on Mulholland Drive renders a woman amnesiac, she and a Hollywood-hopeful search for clues and answers across Los Angeles in a twisting venture beyond dreams and reality.'''


parser = StrOutputParser()

# make 2 seperate parallel chains and then merge their output to a final chain
parallel_chain = RunnableParallel({
    'notes' : prompt1 | model1 | parser,
    'quiz' : prompt2 | model2 | parser
    })

merge_chain = prompt3 | model1 | parser


# final_chain
chain = parallel_chain | merge_chain

result = chain.invoke({'text':text})

print(result)

# to view steps in the chain
chain.get_graph().print_ascii()
    