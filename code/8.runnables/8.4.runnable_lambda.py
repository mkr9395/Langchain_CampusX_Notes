# create custom function where we want to use lambda and count the number of words in the joke
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough, RunnableSequence, RunnableParallel, RunnableLambda
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()
parser = StrOutputParser()

prompt = PromptTemplate(
    template = 'Tell me a joke about {topic}',
    input_variables= ['topic']
    )

# sequential chain to generate the joke
joke_gen_chain = RunnableSequence(prompt, model, parser)


# 2 parallel paths, one for the exact joke and the other for number of words in the joke
parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'word_count': RunnableLambda(lambda x: len(x.split(' '))) # custom function to count the number of words in the joke
})

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

result = final_chain.invoke({'topic':'life'})

print('\n',result['joke'])

print('\n total word count is : ',result['word_count'])

final_chain.get_graph().print_ascii()
