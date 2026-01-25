from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

documents =[
            "Delhi is capital of India",
            "Mumbai is capital of Maharashtra",
            "Paris is capital of France"
           ]

vector = embedding.embed_documents(documents)
print(vector)