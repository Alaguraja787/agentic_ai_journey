#creating the function
def add(a:int, b:int) -> int:
    return a+b

def multiply(a:int, b:int) -> int:
    return a*b

def subtract(a:int, b:int) -> int:
    return a-b

def division(a:int, b:int) ->int:
    return a/b

#create the tool register

tools = {
    "add" : add,
    "multiply" : multiply,
    "subtract" : subtract,
    "division" : division
}

#LLM received information

tool_call = {
    "tool": "multiply",
    "arguments": {"a": 1000, "b": 3}
}

#find the suitable tool and execute it

if not tool_call["tool"] in tools:
    print("Tool not found")
else:
    tool = tools[tool_call["tool"]]
    result = tool(**tool_call["arguments"])
    print(result)
