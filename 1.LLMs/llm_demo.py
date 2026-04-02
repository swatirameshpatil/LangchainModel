from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model='gpt-3.5-turbo-instruct')
prompt = "You are log analyzer, you have to analyze the log, find the RCA from logs and give the solution"
logsample= " 2023-10-01 10:00:00 ERROR: Database connection failed\n2023-10-01 10:05:00 ERROR: Timeout while connecting to the database\n2023-10-01 10:10:00 ERROR: Database connection failed\n"
prompt = f"{prompt}\n\nHere are the logs:\n{logsample}\n\nPlease analyze the logs and provide the RCA and solution."
result = llm.invoke(prompt)
print(result)
