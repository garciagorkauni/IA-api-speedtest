import time
import warnings

from gpt.gpt_chatbot import gpt_response
from llama.llama_chatbot import llama_response
from gemini.gemini_chatbot import gemini_response

# Get user prompt
prompt = input("Prompt for the chatbots: ")

# Calculate the needed time of response of each chatbot
# LLAMA
try:
    start_time = time.time()
    llama_response(prompt)
    end_time = time.time()
    LLAMA_RESPONSE_TIME = end_time - start_time
    print("Llama api response time: {}".format(LLAMA_RESPONSE_TIME))
except:
    print("An error ocurred getting the response of llama...")

# GEMINI
try:
    start_time = time.time()
    gemini_response(prompt)
    end_time = time.time()
    GEMINI_RESPONSE_TIME = end_time - start_time
    print("Gemini api response time: {}".format(GEMINI_RESPONSE_TIME))
except:
    print("An error ocurred getting the response of gemini...")

# GPT
try:
    start_time = time.time()
    gpt_response(prompt)
    end_time = time.time()
    GPT_RESPONSE_TIME = end_time - start_time
    print("GPT api response time: {}".format(GPT_RESPONSE_TIME))
except:
    print("An error ocurred getting the response of gpt...")

print("\n\n")

# print('Llama: ' + llama_response(prompt)
# print('Gemini: ' + gemini_response(prompt)
# print('GPT: ' + gpt_response(prompt)
