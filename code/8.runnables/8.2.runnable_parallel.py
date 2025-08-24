# parallel tweet and linkedin post on the same topic
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableSequence
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()
parser = StrOutputParser()


# for tweet
prompt1 = PromptTemplate(
    template = 'generate a tweet about {topic}',
    input_variables= ['topic']
)

# for linkedin
prompt2 = PromptTemplate(
    template = 'generate a linkedin post about {topic}',
    input_variables= ['topic']
)

# runnable parallel uses a dictionary
parallel_chain = RunnableParallel({
    'tweet' : RunnableSequence(prompt1, model, parser),
    'linkedin' : RunnableSequence(prompt2, model, parser)
})

result = parallel_chain.invoke({'topic':'AI'})

print(result)

print(result['tweet'])
print(result['linkedin'])
parallel_chain.get_graph().print_ascii()