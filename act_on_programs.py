# # from program_files import music, clock, ask_gpt

# # def act_on_programs(keywords:dict, text) -> None:
# #     if keywords["keyword-present"] != False:
# #         keyword = keywords["keyword"]
# #         match keyword:
# #             case "music":
# #                 music.play_music(text)
# #             case "time":
# #                 clock.tell_time()
# #     else:
# #         ask_gpt.ask_gpt(text)

# from program_files import music, clock
# import recognize_keywords, text_to_voice
# import threading

# def init_act_on_program():
#     music.init_music()

# def act_on_programs(keywords:dict, text:str) -> None:
#     is_music_playing = music.music_is_playing()
#     if keywords["keyword-present"] != False:
#         keyword = keywords['keyword']
#         match keyword:
#             case 'time':
#                 # #Create a thread
#                 # #Start the thread
#                 # print('timer detected!')
#                 # time = keyword_filter.find_seconds_in_text(text)
#                 # thread = threading.Thread(target=clock.create_timer, args=[time]) #Setting to 5 for testing
#                 # thread.start()
#                 print('activating timer')
            
#             case 'music':
#                 print('THE STATUS OF THE MIXER IS ', is_music_playing)
#                 if is_music_playing == False:
#                     #music.play_music(text)
#                     print("IS MUSIC PLAYING (ACT ON PROGRAMS):",is_music_playing, "|| Detected music keyword")
#                     thread_music = threading.Thread(target=music.play_music, args=(text,))
#                     thread_music.start()

#         control_words = {'pause':['pause','stop'], 'resume':['start',' unpause', 'resume'], 'stop':['stop','end']}
#         is_music_playing_new = music.music_is_playing()
#         print(is_music_playing_new)
#         if is_music_playing_new == 1:
#             print("MUSIC IS PLAYING (ACT ON PROGRAMS)")
#             for control_word in control_words:
#                 for word in control_words[control_word]:
#                     if word in text:
#                         if control_word == 'pause':
#                             music.pause_music()
#                         elif control_word == 'resume':
#                             music.unpause_music()
#                         elif control_word == 'stop':
#                             music.stop_music()

# def testing():
#     while True:
#         text_input = input('YOU (act_on_progrgams):  ')
#         recognize_keywords.initialising_keyword()
#         keywords = recognize_keywords.recognize_keywords(text_input)
#         init_act_on_program()
#         act_on_programs(keywords, text_input)
#         print("TESTING ACT ON PROGAMS, THE PLAYER IS", music.music_is_playing())

# #testing()

from program_files import music, clock, ask_gpt, weather, news
from recognize_keywords import initialising_keyword, recognize_keywords, find_seconds_in_text
import threading, text_to_voice
from time import sleep
from text_to_voice import Speak

def init_act_on_program():
    music.init_music()
    initialising_keyword()
    

def act_on_programs(keyword_value:str, text:str) -> None:

    match keyword_value:
        
        case 'timer':
            #Create a thread
            #Start the thread
            print('timer detected!')
            time = recognize_keywords.find_seconds_in_text(text)
            thread = threading.Thread(target=clock.create_timer, args=[time]) #Setting to 5 for testing
            thread.start()

        case 'music':
            print('THE STATUS OF THE MIXER IS ', music.music_is_playing())
            sleep(1)
            if music.music_is_playing() == False:
                #music.play_music(text)
                thread_music = threading.Thread(target=music.play_music, args=(text,))
                thread_music.start()


        case 'gemini':
            ask_gpt.ask_gpt(text)

        case 'weather':
            weather.weather(text)
        
        case 'news':
            news.news()


    control_words = {'pause':['pause', 'boss'], 'resume':['resume'], 'stop':['stop','end']}
    for control_word in control_words:
        for word in control_words[control_word]:
            if music.music_is_playing():
                if word in text:
                    if control_word == 'pause':
                        music.pause_music()
                    elif control_word == 'stop':
                        music.stop_music()
            elif control_word == 'resume':
                music.resume_music()