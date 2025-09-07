from dotenv import load_dotenv
import os
from google import genai

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=api_key)

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

response = client.models.generate_content(
    model = "gemini-2.0-flash",
    contents=[
        systempromt,
       "What is 3 + 4 * 5?"

       #
       {"role": "assistant", "content": json.dumps({"step": "analyse", "content": "The user is asking to solve a mathematical expression involving addition and multiplication. We need to follow the order of operations (PEMDAS/BODMAS) to get the correct answer." })}
    ]

)

print(response.text)