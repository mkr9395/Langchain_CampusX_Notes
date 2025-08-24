from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path = 'Social_Network_Ads.csv')

data = loader.load()

# for every row in csv we get 1 document object
print(len(data))
print(data[0])

print(data[1])
print(data[1].metadata)