import time
import warnings

from gpt.gpt_chatbot import gpt_response
from llama.llama_chatbot import llama_response
from gemini.gemini_chatbot import gemini_response

# Get user prompt
prompt = input("Prompt for the chatbots: ")

# Get and show the response of each chatbot
# LLAMA
try:
    print("LLAMA:\n" + llama_response(prompt))
except:
    print("An error ocurred getting the response of llama...")

# GEMINI
try:
    print("GEMINI:\n" + gemini_response(prompt))
except:
    print("An error ocurred getting the response of gemini...")

# GPT
try:
    print("GPT:\n" + gpt_response(prompt))
except:
    print("An error ocurred getting the response of gpt...")

print("\n\n")
