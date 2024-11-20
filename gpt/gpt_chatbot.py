import os
from openai import OpenAI

def gpt_response(prompt):
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    chat_history = []

    while True:
        chat_history.append({"role": "user", "content": prompt})

        response_iterator = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": "Say this is a test",
                }
            ],
            # model="gpt-4o",
            model="gpt-3.5-turbo",
        )

        collected_messages = []

        for chunk in response_iterator:
            chunk_message = chunk['choices'][0]['delta']
            collected_messages.append(chunk_message)
            full_reply_content = ''.join([m.get('content', '') for m in collected_messages])
            print(full_reply_content)

            print("\033[H\033[J", end="")

        chat_history.append({"role": "assistant", "content": full_reply_content})

        return full_reply_content
