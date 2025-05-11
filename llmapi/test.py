from openai import OpenAI
import openai
import os
from dotenv import load_dotenv


api_key = "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"


#load_dotenv()


client = OpenAI(api_key=api_key)


response = client.responses.create(
  model="gpt-4.1",
  input="Tell me a three sentence bedtime story about a unicorn."
)

print(response)
