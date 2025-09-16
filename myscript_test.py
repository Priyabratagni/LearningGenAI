# from openai import OpenAI
# from dotenv import load_dotenv

# load_dotenv()
# client = OpenAI()

# response = client.chat.completions.create(
#     model="gpt-4",
#     messages=[
#         {"role": "user", "content": "Write a short story on Hinduism"}
#     ]
# )

# print(response.choices[0].message.content)


from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="gpt-4o",
    input="Write a one-sentence bedtime story about a unicorn."
)

print(response.output_text)