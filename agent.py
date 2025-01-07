from typing_extensions import TypedDict

from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI

## Tools
from tools.dalle_image_generator import generate_dalle_image
from tools.duckduckgo_search import duckduckgo_search
# from tools.python_interpreter import repl_tool

tools=[duckduckgo_search, generate_dalle_image]

# Instantiate LLM
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

system_prompt="Ensure your generation of the image URL is exact, add an extra space after it to ensure no new lines mess it up."

# Main Graph
langent = create_react_agent(llm, tools, messages_modifier=system_prompt)
