from langchain_core.tools import tool 
from langchain_ollama import ChatOllama
#from langgraph.prebuilt import create_react_agent
from langchain.agents import create_agent

# Define tool
# @tool
# def multiply(a: int, b: int) -> int:
#     """Multiply two numbers"""
#     return a * b

@tool
def calculator(expression: str) -> float:
    """Evaluate a mathematical expression"""
    return eval(expression)

model = ChatOllama(model="qwen3:1.7b")

tools = [calculator]

# agent = create_react_agent(model, tools) 
agent = create_agent(model, tools)

query = "what is (2+8) multiplied by 9?"
response = agent.invoke({"messages": [("human", query)]})

print(response['messages'][-1].content)