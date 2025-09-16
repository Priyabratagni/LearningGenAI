from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()

client = OpenAI()

systempromt = """

You are an AI Assitant who generate multiple responses and choose the most common answer from all of them.

For the given input you give multiple answers and try to find commonalities and give final answer.

You give 4 responses for a given user input and out of these you find common answer and provides a final output.

Output Format:
Your output should always be a JSON object with the following structure: {{ step: "string", content: "string"}}

Example:
Input: When I was 6 my sister was half my age. Now I’m 70 how old is my sister?
Output: {{"Step": "output 1","content": "1: Since the user was 6 and their sister was half of their age at that time, we need to find the age gap between the user and their sister and apply it to the current age of the user to determine the current age of the sister. My sister is currently 64 years old."}}
Output: {{"Step": "output 2","content": "2: When I was 6 my sister was half my age, so she was 3. Now I am 70, so she is 70/2 = 35. The answer is 35."}}
Output: {{"Step": "output 3","content": "3: When I was 6 my sister was half my age, so she was 3. Now I am 70, so she is 70 - 3 = 67. The answer is 67."}}
Output: {{"Step": "output 4","content": "4: When the narrator was 6, his sister was half his age, which is 3. Now that the narrator is 70, his sister would be 70 - 3 = 67 years old. The answer is 67."}}

Output: {{"Step": "Final Output","content": "Final Output: Since the common response was 67 years. Hence the final answer will be 67 years old."}}
"""


message= [
    {"role": "system", "content": systempromt}
]

query = input("> ")
message.append({"role": "user", "content": query})


while True:
    response = client.chat.completions.create(
        model="gpt-4o",
        response_format={"type": "json_object"},
        messages= message
    )


    parsed_response=json.loads(response.choices[0].message.content)
    message.append({"role": "assistant", "content": json.dumps(parsed_response)})

    if parsed_response.get("step") != "Final Output":
        print(f"🧠: {parsed_response.get('content')}")
        continue

    print(f"🤖: {parsed_response.get('content')}")
    break