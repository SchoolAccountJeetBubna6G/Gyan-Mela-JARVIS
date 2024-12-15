def init_ask_gpt():
    import google.generativeai as genai
    API_KEY = "AIzaSyAXH2_eCdbt1PDurwk0FoGtMHEo-GxglRI"
    genai.configure(api_key=API_KEY)
    global model
    model = genai.GenerativeModel("gemini-1.5-flash")

def ask_gpt(text):
    if text != None:
        response = model.generate_content(text + '. please do not include any formatting, including * or --')
        from text_to_voice import Speak
        Speak(str(response.text))
    else:
        return