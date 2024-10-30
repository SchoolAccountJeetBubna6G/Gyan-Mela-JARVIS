import google_search
import music_player
import clock
import volume_shifter
import weather_fetcher
import keyword_filter
import threading
import noris_speak as ns


def keyword_to_program_linker(keyword_value:str, text:str) -> None:

    match keyword_value:
        
        case 'weather_fetcher.py':
            weather_fetcher.fetch_weather(text)


        case 'volume_shifter.py':
            volume_shifter.volume_shift(text)

        
        case 'timer.py':
            #Create a thread
            #Start the thread
            print('timer detected!')
            time = keyword_filter.find_seconds_in_text(text)
            thread = threading.Thread(target=clock.create_timer, args=[time]) #Setting to 5 for testing
            thread.start()

        case 'music_player.py':
            print('THE STATUS OF THE MIXER IS ', music_player.IS_PLAYING)
            if music_player.IS_PLAYING == False:
                #music_player.play_music(text)
                print(music_player.IS_PLAYING)
                thread_music = threading.Thread(target=music_player.play_music, args=(text,))
                thread_music.start()


        case 'google_search.py':
            pass


    control_words = {'pause':['pause','stop'], 'resume':['start',' unpause', 'resume'], 'stop':['stop','end']}
    if music_player.IS_PLAYING:
        for control_word in control_words:
            for word in control_words[control_word]:
                if word in text:
                    if control_word == 'pause':
                        music_player.pause_music()
                    elif control_word == 'resume':
                        music_player.unpause_muisc()
                    elif control_word == 'stop':
                        music_player.stop_music()

#keyword_to_program_linker('music_player.py', 'pause music')