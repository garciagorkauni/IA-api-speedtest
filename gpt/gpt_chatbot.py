import os
from openai import OpenAI

def gpt_response(prompt):
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    chat_history = []
    chat_history = [{"role": "user", "content": prompt}]

    response = client.chat.completions.create(
        messages=chat_history,
        # model="gpt-4o",
        model="gpt-3.5-turbo",
    )

    full_reply_content = response['choices'][0]['message']['content']
    return full_reply_content
