import os
from llamaapi import LlamaAPI

def llama_response(prompt):
    llama = LlamaAPI(os.getenv('LLAMA_API_KEY'))

    api_request_json = {
        "messages": [
            {"role": "user", "content": prompt},
        ]
    }
    
    response = llama.run(api_request_json)
    assistant_response = response.json()['choices'][0]['message']['content']
    
    return assistant_response

