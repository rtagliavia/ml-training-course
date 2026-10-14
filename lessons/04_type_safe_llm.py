"""Type-safe LLM classification with Grok (xAI).
Requires XAI_API_KEY in env.
pip install xai-sdk pydantic
"""
import os
from typing import Literal
from pydantic import BaseModel
from xai_sdk import Client
from xai_sdk.chat import user

if not os.getenv("XAI_API_KEY"):
    print("Set XAI_API_KEY to run this example.")
    exit(0)

client = Client(api_key=os.getenv("XAI_API_KEY"))

class Sentiment(BaseModel):
    label: Literal["positive", "negative", "neutral"]
    confidence: float

text = "The product arrived late and was damaged."

chat = client.chat.create(
    model="grok-4.7",
    response_format=Sentiment,
)
chat.append(user(f"Classify sentiment of: {text}"))

response = chat.sample()
result = Sentiment.model_validate_json(response.content)
print(result)
print("Type-safe Grok output:", result.label)
