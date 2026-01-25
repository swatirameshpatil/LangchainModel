from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=300)
"""documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]"""

_pdf_path = "/Users/rameshpatil/Downloads/swift-ug-cbpr.pdf"
documents = PyPDFLoader(_pdf_path).load()
#print("PDF Data: ",documents)
#query= "tell me about Bank to Customer Account Report. Also format the result as per section instea of raw string"
query = "give me sample for Bank to Customer Account Report"
texts = [d.page_content for d in documents]   # convert Document -> str
#doc_embedding = embedding.embed_documents(texts)

doc_embedding = embedding.embed_documents(texts)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding], doc_embedding)[0]
index, score = sorted(list(enumerate(scores)), key=lambda x:x[1])[-1]
print(query)
print(documents[index])
print("Similarity score: ",score)