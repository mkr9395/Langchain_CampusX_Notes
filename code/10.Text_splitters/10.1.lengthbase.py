from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('D:\Generative AI\CampusX\GenerativeAI_using_Langchain\code\9.Documentloader\dl-curriculum.pdf')

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size = 200,
    chunk_overlap = 0,
    separator = ''
)

result = splitter.split_documents(docs)

print(result[1].page_content)

print(result[2].metadata)