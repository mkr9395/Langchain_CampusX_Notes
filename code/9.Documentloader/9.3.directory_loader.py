# load all the files present inside a folder/directory
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader


loader = DirectoryLoader(
    path = 'D:\Books\deep learning',
    glob = '*.pdf',
    loader_cls = PyPDFLoader
)


docs = loader.load()

print(len(docs))

# first pdf 1st page

print(docs[0].page_content)

print('metadata : ', docs[0].metadata)


# now using lazy_load -> loads pages one by one
docs = loader.lazy_load()

for i in docs:
    print(i.metadata)