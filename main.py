from voice_to_text import voice_to_text, voice_recognition_init
from recognize_keywords import recognize_keywords, initialising_keyword
from act_on_programs import act_on_programs, init_act_on_program
from keyword_detection import hotword_in, keyword_has_been_said_in
from text_to_voice import Speak
from program_files.ask_gpt import init_ask_gpt
from program_files.music import init_music
import vlc
player = None

HOTWORDS = ['jarvis', 'jar is', 'joggers','giants', 'job is', 'chargers', 'divers', 'joy this']
BUFFER_TIME_FOR_SPEECH = 10 #Seconds

def main_loop(text):
    try:
        #text = input('YOU:: ')
        #print(text)
        # if hotword_in(text, HOTWORDS):
        #     recognized_keywords = recognize_keywords(text)
        #     act_on_programs(recognized_keywords, text)
        recognized_keywords = recognize_keywords(text)
        act_on_programs(recognized_keywords, text)
        if 'pause' in text:
            player.set_pause(1)
    except Exception:
         return None

def init():
    init_ask_gpt()
    voice_recognition_init("google")
    initialising_keyword()
    init_act_on_program()
    init_music()
    global player
    player = vlc.MediaPlayer()

def main():

    init()
    Speak('Hello sir, how may i help you?')
    

    _ = True
    while _:
        if keyword_has_been_said_in(BUFFER_TIME_FOR_SPEECH):
                #text = input("YOU: ")
                text = voice_to_text("google")
                print(text)
                recognized_keywords = recognize_keywords(text)
                if recognized_keywords['keyword-present'] == True:
                    print('reached here -- keyword detected')
                    if recognized_keywords['keyword'] == "terminate":
                         print('terminating')
                         _ = False 
                         return
                    act_on_programs(recognized_keywords['keyword'], text)
        else:
                main_loop('shababaoi')
        
if __name__ == '__main__':
    main()      
