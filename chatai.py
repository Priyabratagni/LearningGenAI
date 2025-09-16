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

result = client.chat.completions.create(
    model="gpt-4o",
    response_format={"type": "json_object"},
    messages=[
        {"role": "system", "content": systempromt},
        {"role": "user", "content": "What is 3 + 5 * 2?"},

        #
        {"role": "assistant", "content": json.dumps({"step": "analyse", "content": "The user is asking about the arithmetic expression involving both addition and multiplication: 3 + 5 * 2. This requires understanding the order of operations."})},
        {"role": "assistant", "content": json.dumps({"step": "think", "content": "I need to recall the order of operations, which is usually summarized as PEMDAS/BODMAS - Parentheses/Brackets, Exponents/Orders, Multiplication and Division (from left to right), Addition and Subtraction (from left to right)."})},
        {"role": "assistant", "content": json.dumps({"step": "think", "content": "According to the order of operations, multiplication should be performed before addition."})},
        {"role": "assistant", "content": json.dumps({"step": "think", "content": "First, I will evaluate the multiplication part of the expression: 5 * 2."})},
        {"role": "assistant", "content": json.dumps({"step": "output", "content": "5 * 2 = 10"})},
        {"role": "assistant", "content": json.dumps({"step": "think", "content": "Now, I will perform the addition part of the expression: 3 + 10."})},
        {"role": "assistant", "content": json.dumps({"step": "output", "content": "3 + 10 = 13"})},
        {"role": "assistant", "content": json.dumps({"step": "validate", "content": "The evaluation followed the correct order of operations: first multiplication, then addition, resulting in 13."})},
        {"role": "assistant", "content": json.dumps({"step": "results", "content": "3 + 5 * 2 = 13 has been calculated following the proper mathematical order of operations: multiplication before addition."})},
        

    ]
)

print(result.choices[0].message.content)