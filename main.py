from langchain_core.tools import tool 
from langchain_ollama import ChatOllama
from langgraph.prebuilt import create_react_agent
import os 
from dotenv import load_dotenv

load_dotenv()

model = ChatOllama(
    model="phi3:mini",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

tools = []  

agent = create_react_agent(model, tools)

query = "what is (2+8) multiplied by 9?"
response = agent.invoke({"messages": [("human", query)]})

print(response['messages'][-1].content)