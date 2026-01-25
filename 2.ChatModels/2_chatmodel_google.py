from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
llm = ChatGoogleGenerativeAI(model='gemini-3-pro-preview')
result = llm.invoke("What is capital of India")
print(result.content)