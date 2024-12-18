import os
import tempfile
from text_to_voice import Speak

def init_ask_gpt():
    import google.generativeai as genai
    API_KEY = "AIzaSyAXH2_eCdbt1PDurwk0FoGtMHEo-GxglRI"
    genai.configure(api_key=API_KEY)
    global model
    model = genai.GenerativeModel("gemini-1.5-flash")
    global chats
    chats = []

def ask_gpt(text):
    print('gemini')
    if text != None:
        text = f'THE USERS PREVIOUS CHATS: {chats}' + text
        response = model.generate_content('You are a personal assistant, more specificly JARVIS from the IRON man movies. The previous conversations with the user are given in the list Ahead. Please try to respond in the most movie accurate way and answer any specific questions related to jarvis (like what is the full form of it, how are you doing? etc.) in character . please do not include any formatting, including * or --: '+text)
        response = response.text.strip()
        chats.append({"USER": text, "YOU":response})
        _ = response
        Speak(_)
    else:
        return
    
def testing(x):
    init_ask_gpt()
    ask_gpt(x)

