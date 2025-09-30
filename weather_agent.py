from openai import OpenAI
from dotenv import load_dotenv
import json
from datetime import datetime
import requests

load_dotenv()

client = OpenAI()

# Fucntion to call wether api
def get_weather(city: str):
    # TODO: Do an actual api-call
    url = f"https://wttr.in/{city}?format=%C+%t" 
    response = requests.get(url)

    if response.status_code == 200:
        return f"The Weather of {city} is {response.text}"
    
    return "Something went wrong"

available_tools = {
    "get_weather" : get_weather,
    # "run_command" : run_command
}

system_prompt="""
    You are an AI Assistant who specialized in resolving user query.
    You follow the step plan, action, Observe and output.

    For the given user query, follow step by step execution.
    Plan the steps, perform action by selecting relevant tool from the available tools and perform action. 
    Wait for observation and based on the observation, give the output and resolve the user query.

    Follow these steps:
    - Follow the JSON Format
    - Always perform one step at a time and wait for next input
    - Carefully analyse the user query

    Output JSON format:
    {{
        "step": "string",
        "content":"string",
        "function": "Name of the function if the step is action."
        "input": "The input parameter for the function"
    }}

    Available Tools:
    - "get_weather": Takes a city name as a input and returns the current whether for the city
    - "run_command": Takes Linux command as a string and executes the command and returns the output after executing it.

    Example:
    User Query: What is the weather of new york?
    Output: {{ "step": "plan", "content": "The user is interseted in weather data of new york" }}
    Output: {{ "step": "plan", "content": "From the available tools I should call get_weather" }}
    Output: {{ "step": "action", "function": "get_weather", "input": "new york" }}
    Output: {{ "step": "observe", "output": "12 Degree Cel" }}
    Output: {{ "step": "output", "content": "The weather for new york seems to be 12 degrees." }}
 
"""

# Api calling
message=[
    {"role":"system", "content":system_prompt}
]

#user input
query = input("> ")
message.append({"role":"user", "content": query})

while True:
    response = client.chat.completions.create(
        model="gpt-4o",
        messages= message,
        response_format={"type":"json_object"}
    )
    
    parsed_response = json.loads(response.choices[0].message.content)
    message.append({"role":"assistant","content":json.dumps(parsed_response)})

    if parsed_response.get("step") == "plan":
        print(f"🧠🧠🧠: {parsed_response.get('content')}")
        continue

    if parsed_response.get("step") == "action":
        tool_name = parsed_response.get("function")
        tool_input = parsed_response.get("input")

        print(f"🪓🪓🪓: calling tool {tool_name} with input {tool_input}")

        if available_tools.get(tool_name) != False:
            output = available_tools[tool_name](tool_input)
            message.append({"role": "user", "content": json.dumps({"step": "observe", "output": output})})
            continue

    if parsed_response.get("step") == "output":
        print(f"🤖🤖: {parsed_response.get('content')}")
        break

    print("--------------------------------------------------------------------------")