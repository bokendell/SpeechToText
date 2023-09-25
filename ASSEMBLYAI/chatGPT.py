import openai
import os
import pandas as pd
import time

openai.api_key = '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'

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]

    response = openai.ChatCompletion.create(
    model=model,
    messages=messages,
    temperature=0,
    )   
    return response.choices[0].message["content"]