from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()


model = ChatOpenAI(model='gpt-4')
result = model.invoke("what is the capital of india?")
print(result.content)  # Access the content of the response



### For Anthropic (Claude)

# from langchain_anthropic import ChatAnthropic
# from dotenv import load_dotenv

# load_dotenv()

# model = ChatAnthropic(model='claude-3-5-sonnet-20241022')

# result = model.invoke('What is the capital of India')

# print(result.content)