"""Type-safe LLM classification example.
Requires OPENAI_API_KEY in env.
Install: pip install openai instructor pydantic
"""
import os
from typing import Literal
import instructor
from openai import OpenAI
from pydantic import BaseModel

# Set your key: export OPENAI_API_KEY=sk-...
if not os.getenv("OPENAI_API_KEY"):
    print("Set OPENAI_API_KEY to run this example.")
    exit(0)

client = instructor.from_openai(OpenAI())

class Sentiment(BaseModel):
    label: Literal["positive", "negative", "neutral"]
    confidence: float

text = "The product arrived late and was damaged."

result = client.chat.completions.create(
    model="gpt-4o-mini",
    response_model=Sentiment,
    messages=[{"role": "user", "content": f"Classify sentiment: {text}"}]
)
print(result)
print("Type-safe output:", result.label)
