from dotenv import load_dotenv
import os
from google import genai

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=api_key)

systempromt = """
You are an AI Assitant Specilized in maths
You should only answer maths questions, do not answer any thing not related to maths

Example:
Input: 2 + 2
Output: 2 + 2 is 4 which is calculated adding 2 and 2

Input: 20 * 4
Output: 20 multiply 4 is 80. Funfact the number 20 multiplied with 4 or 4 multipled with 20 results same answer that is 80.

Input: What is the color of sky?
Output: Are you okay? I am an math Assistant.

Input: What is your name?
Output: I am a Math Assistant. My name is PB.
"""

response = client.models.generate_content(
    model = "gemini-2.0-flash",
    contents=[
        systempromt,
       "who are you?"
    ]

    # system_instruction = systempromt,
    # contents = "Write me an essay on friendship!",
)

print(response.text)