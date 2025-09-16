from dotenv import load_dotenv
from myscript_test import OpenAI

load_dotenv()

client = OpenAI()

results = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", 
         "content": "Hey there, How are you?"}
    ]
)

print(results.choices[0].message.content)