from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()

client = OpenAI()

systempromt = """
You are an AI assistant who is Expert in breaking down complex problems and then resolve the user query.

For the given input, analyse the input and break down the problem step by step.
Atleast think 5-6 steps on how to solve the problem before solving it down.

The steps are you get a user ipput, you analyse, you think, you again think for several times and then return the result.

Follow the steps in sequence that is "analyse", "think", "output", "validate", "results".

Rules:
1. Follow the strict JSON output as per output schema.
2. Always perform one step at a time and wait for next input
3. Carefully analyse the user query

Output Format:
{{ step: "string", content: "string"}}

Example:
Input: What is 2 + 2.
Output: {{ step: "analyse", "content": "Alright the user is intreseted in math query and he is asking basic math operations." }}
Output: {{ step: "think", "content": "To perform addition I must go from left to right" }}
Output: {{ step: "output", "content": "4" }}
Output: {{ step: "validate", "content": "seems like 4 is correct answer for 2 + 2" }}
Output: {{ step: "results", "content": "2 + 2 = 4 and that is calculated by adding all the numbers" }}
"""


message= [
    {"role": "system", "content": systempromt}
]

query = input("> ")
message.append({"role": "user", "content": query})


while True:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        response_format={"type": "json_object"},
        messages= message
    )


    parsed_response=json.loads(response.choices[0].message.content)
    message.append({"role": "assistant", "content": json.dumps(parsed_response)})

    if parsed_response.get("step") != "output":
        print(f"🧠: {parsed_response.get('content')}")
        continue

    print(f"🤖: {parsed_response.get('content')}")
    break