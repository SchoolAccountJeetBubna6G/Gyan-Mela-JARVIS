from program_files.music import play_music, pause_music, stop_music, music_is_playing, init_music
from voice_to_text import voice_to_text, voice_recognition_init, manual_input_test
from recognize_keywords import recognize_keywords, initialising_keyword
import threading

def init_thread_program():
    initialising_keyword()
    init_music()
    voice_recognition_init('google')

def thread_programs(text:str) -> None:
    
    play_music_thread = threading.Thread(target=play_music, args=[text])
    pause_music_thread = threading.Thread(target=pause_music)
    stop_music_thread = threading.Thread(target=stop_music)
    voice_recognition = threading.Thread(target=manual_input_test, args=['google'])

    keyword_data = recognize_keywords(text)
    voice_recognition.start()
    print(keyword_data)
    if keyword_data['keyword-present'] == True:
        keyword = keyword_data['keyword']
        match keyword:
            case 'music': 
                if music_is_playing():
                    pause_music_thread.start()
                elif 'stop' in text:
                    stop_music_thread.start()
                else:
                    play_music_thread.start()


    return {
        "play_music":play_music_thread,
        "pause_music":pause_music_thread,
        "stop_music":stop_music_thread,
        "voice_recognition":voice_recognition
    }

init_thread_program()

#thread_programs(input('YOU:: (present in threading program):: '))