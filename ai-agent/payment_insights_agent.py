import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path)

api_key = os.getenv("OPENAI_API_KEY")

print("API KEY FOUND:", api_key is not None)

client = OpenAI(api_key=api_key)

prompt = """
You are a Senior Payments Analytics Consultant.

Analyze the following metrics:

Merchant Revenue:
BigBasket - 1917130
Myntra - 1707650
Flipkart - 2092987
Zomato - 1563003
Swiggy - 2103717

City Revenue:
Bangalore - 2661394
Mumbai - 2270854
Hyderabad - 2280141

Status Counts:
SUCCESS - 180
FAILED - 168
PENDING - 170

Provide:
1. Key business insights
2. Revenue trends
3. Potential operational concerns
4. Executive summary
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a payments analytics expert."},
        {"role": "user", "content": prompt}
    ]
)

print("\n")
print(response.choices[0].message.content)