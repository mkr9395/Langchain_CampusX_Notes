# to give the joke and explanantion both
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough, RunnableSequence, RunnableParallel
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()
parser = StrOutputParser()


prompt1 = PromptTemplate(
    template = 'Tell me a joke about {topic}',
    input_variables= ['topic']
    )

prompt2 = PromptTemplate(
    template = 'Explain the following joke = {text}',
    input_variables= ['text']
    )
# sequential chain to generate the joke
joke_gen_chain = RunnableSequence(prompt1, model, parser)

# 2 parallel paths, one for the exact joke and the other for explanantion
parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'explanation': RunnableSequence(prompt2, model, parser)
})

# now connecting joke_gen_chain and parallel_chain

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

result = final_chain.invoke('Cricket')

print('\n',result['joke'])

print('\n',result['explanation'])

parallel_chain.get_graph().print_ascii()

