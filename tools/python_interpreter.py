from langchain_core.tools import tool, Tool
from langchain_experimental.utilities import PythonREPL

python_repl = PythonREPL()

repl_tool = Tool(
    name="python_repl",
    description="A Python shell. Use this to execute python commands. Input should be valid python commands. ALWAYS print ANY results out with `print(...)`",
    func=python_repl.run,
)