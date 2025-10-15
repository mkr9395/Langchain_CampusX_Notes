from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage
# chat template
chat_template = ChatPromptTemplate([
    ('system','You are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'), # all previous chats in this placeholder, all chats will be inserted here
    ('human','{query}')
])

chat_history = []
# load chat history
with open(r'D:\Generative_AI\CampusX\Langchain_Campusx\code\4.prompts\6.1.chat_history.txt') as f:
    chat_history.extend(f.readlines())

# print(chat_history)

# create prompt
prompt = chat_template.invoke({'chat_history':chat_history, 'query':'Where is my refund'})

print(prompt)

