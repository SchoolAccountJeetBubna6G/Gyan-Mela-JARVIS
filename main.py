#------------------------------------
import speech
from keyword_filter import keyword_in_text, assistant_name_in_text, __init__
import keyword_to_program
#!--------------------------------------------------------------------------------------------------------------------------

PATH_TO_MODEL = r'C:\Users\Jeet\Desktop\Projects\PythonProjects\SpeechRecognition\Hitler Mk2 - Noris\vosk-model-en-in-0.5'
ASSISTANT_NAME = ['hitler','littler','peddler','riddler', 'butler', 'nadler', 'headley', 'edler', "he'd learn", "atla"]     #The names that can be misinterprited by the model.

speech.__init__(PATH_TO_MODEL, method='google')
__init__() #Initializes keyword filter

def main(): 
    #text = speech.generate_text_vosk()
    text = speech.generate_text_google()
    #text = input('YOU:: ')
    if type(text) is str:
        text = text.lower()
        print(text, assistant_name_in_text(ASSISTANT_NAME, text))#Debug
        if assistant_name_in_text(ASSISTANT_NAME, text):
            keyword_data = keyword_in_text(text)
            print(keyword_data)
            if keyword_data['keyword_present']:     
                keyword_to_program.keyword_to_program_linker(keyword_value=keyword_data['keyword_value'], text=text)

while True:
    main()