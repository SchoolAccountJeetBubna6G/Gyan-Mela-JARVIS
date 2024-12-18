from voice_to_text import voice_to_text, voice_recognition_init
from recognize_keywords import recognize_keywords, initialising_keyword
from act_on_programs import act_on_programs, init_act_on_program
from keyword_detection import hotword_in, keyword_has_been_said_in
from text_to_voice import Speak
from program_files.ask_gpt import init_ask_gpt
from program_files.music import init_music, play_song, stop_music
import vlc
player = None

HOTWORDS = ['jarvis', 'jar is', 'joggers','giants', 'job is', 'chargers', 'divers', 'joy this', 'Jarvis']
BUFFER_TIME_FOR_SPEECH = 10 #Seconds

def main_loop(text):
    try:
        #text = input('YOU:: ')
        #print(text)
        # if hotword_in(text, HOTWORDS):
        #     recognized_keywords = recognize_keywords(text)
        #     act_on_programs(recognized_keywords, text)
        recognize_keywords = recognize_keywords(text)
        act_on_programs(recognize_keywords, text)
        if 'pause' in text:
            player.set_pause(1)
    except Exception:
         return None

def init():
    init_ask_gpt()
    voice_recognition_init(method="google")
    initialising_keyword()
    init_act_on_program()
    init_music()
    global player
    player = vlc.MediaPlayer()

def cool_start():
    print('cool asss start')
    play_song(r'C:\Users\Dell\Desktop\JEET\JarvisRefactored\songs\downloads\JARVIS START UP.mp3',volume=50)
    from time import sleep
    sleep(17)
    stop_music()
    Speak("Hello sir! what a wonderful day..... This is a gyan mela project, which is made by Jeet Bubna of 9C..... Inspired by Iron Man")
    return
    

def main():

    init()
    cool_start()
    #Speak('Hello sir, how may i help you?')    
    print('ready')
    
    #cool_start()

    _ = True
    while _:
        text = input("YOU: ")
        #text = voice_to_text("google")
        try:
            print(text)
            # for hotword in HOTWORDS:
            #     try:
            #         for word in text.split():
            #             #if word == hotword:
            #             if word == hotword:
            #                 recognized_keywords = recognize_keywords(text)
            #                 if recognized_keywords['keyword-present'] == True:
            #                     print('reached here -- keyword detected')
            #                     if recognized_keywords['keyword'] == "terminate":
            #                         print('terminating')
            #                         _ = False 
            #                         return
            #                     act_on_programs(recognized_keywords['keyword'], text)
            #     except Exception:
            #         pass
            recognized_keywords = recognize_keywords(text)
            if recognized_keywords['keyword-present'] == True:
                print('reached here -- keyword detected')
                if recognized_keywords['keyword'] == "terminate":
                    print('terminating')
                    _ = False 
                    return
                act_on_programs(recognized_keywords['keyword'], text)
        except Exception as e:
            print('chutiya benchod speak something na motherchod', e)
        
if __name__ == '__main__':
    main()      
