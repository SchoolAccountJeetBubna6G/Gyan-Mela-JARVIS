#from ..text_to_voice import Speak
from pytubefix import YouTube 
import vlc
from time import sleep
import os
import pygame
import random
from text_to_voice import Speak

# def Speak(data):
#     voice = 'en-US-JennyNeural'
#     file_path = rf"C:\Users\Dell\Desktop\JEET\JarvisRefactored\voice_segments\{random.randint(100000,999999)}"
#     command = f'edge-tts --voice "{voice}" --text "{data}" --write-media {file_path}'
#     os.system(command)

#     pygame.init()
#     pygame.mixer.init()
#     pygame.mixer.music.load(file_path)

#     try:
#         pygame.mixer.music.play()

#         while pygame.mixer.music.get_busy():
#             pygame.time.Clock().tick(10)

#     except Exception as e:
#         print(e)
#     finally:
#         pygame.mixer.music.stop()
#         pygame.mixer.quit()




LOCAL_DOWNLOADS_PATH = r'C:\Users\Dell\Desktop\JEET\JarvisRefactored\songs\downloads'
LOCAL_PLAYLIST_PATH = r"C:\Users\Dell\Desktop\JEET\JarvisRefactored\songs\playlists"
ISPAUSED = False

def init_music():
    global player, instance
    instance = vlc.Instance()
    player = instance.media_player_new()

def find_song_name_in(text:str) -> str:
    ## Returns song name
    try:
        position_of_play = text.split().index('play')           #finds the index of play
        song_name = text.split()[position_of_play+1:]           #finds the name of the song, ie everything after play
        if 'music' in song_name:
            return None
        return ' '.join(song_name)                              #Converts the list into a string
    except Exception as e:
        print('Error ocurred in find_song_name_in:: Try adding play to the command', e)
        return None

def find_playlist_name_in(text:str) -> str:
    return find_song_name_in(text)

def play_playlist(text:str, playlist_name='def'):
    if playlist_name == 'def':
        import os
        files = os.listdir(LOCAL_PLAYLIST_PATH)
        for file in files:
            play_song(rf'{LOCAL_PLAYLIST_PATH}\{file}')
            print(file)
        pass
    
def play_song(music_file_path:str, volume:float=100):
    print(f'the path of the file is: {music_file_path}')
    print('playing rn')

    media = instance.media_new(music_file_path)

    # Set the media to the player
    player.set_media(media)
    player.play()
    # Play the media

def song_is_downloaded(song_name:str) -> bool:
    import os
    file_names = os.listdir(LOCAL_DOWNLOADS_PATH)
    for file in file_names:
        if song_name.lower() in file.lower():
            return [True, file]
    return [False]

def download_song(song_name:str):
    def download(song_name=''):
        yt = YouTube(url=f'https://www.youtube.com/watch?v={getVidID(song_name)}')

        # extract only audio 
        video = yt.streams.filter(only_audio=True).first() 

        # check for destination to save file 
        #print("Enter the destination (leave blank for current directory)") 
        destination = LOCAL_DOWNLOADS_PATH

        # download the file 
        out_file = video.download(output_path=destination) 

        # save the file 
        # base, ext = os.path.splitext(out_file) 
        # new_file = base + '.wav'
        # os.rename(out_file, new_file) 

        # result of success 
        print(yt.title + " has been successfully downloaded.")
        return out_file

    def getVidID(song):
        from youtubesearchpython import VideosSearch
        videosSearch = VideosSearch(f'{song} lyrics', limit = 2)
        return videosSearch.result()['result'][0]['id']

    print("Downloading " + song_name)
    song_path = download(song_name)
    return song_path


def play_music(text:str, vol:int=100):
    print('playing music')

    PLAYLIST_WORDS = ['tunes','music']
    for word in text:
        for keyword in PLAYLIST_WORDS:
            if word == keyword:
                play_playlist(text)
                return
    print(f"{ISPAUSED} --- ISPAUSED (126 MUSIC / play music)")
    if music_is_playing() == False and ISPAUSED == False:
        song_name = find_song_name_in(text)
        print("song_name is,",song_name)
        try:
            Speak('playing '+ song_name)
        except Exception:
            pass
        if song_name == None:
            print("FOUND NO NAME SONG NAME")
            #Its a playlist
            playlist = find_playlist_name_in(text)
            if playlist == None:
                #Default playlist
                Speak("playing default playlist")
                play_playlist(text)
            else:
                try:
                    play_playlist(text, playlist) #if playlist dont exist, just say error no playlist like this exists
                except Exception:
                    Speak("There is no such playlist.")
        else: #song name is there
            print("DELETE LATER 148 ---- MUSIC")
            try:
                print(song_is_downloaded(song_name))
                song_present = song_is_downloaded(song_name)[0]
                if (song_present):
                    song_path = song_is_downloaded(song_name)[1]
                    print(song_path)
                    play_song(rf'{LOCAL_DOWNLOADS_PATH}\\{song_path}', vol)
                else:
                    Speak('downloading song '+ song_name)
                    print('downloading song ', song_name)
                    song_path = download_song(song_name)
                    Speak('download complete, playing song')
                    print('download complete, playing song')
                    play_song(song_path, vol)
            except Exception as e:
                print('AN ERROR OCCURRED IN PLAY MUSIC', e)

def music_is_playing() -> bool:
    #print("PLAYER STATUS, MUSIC 151, the player status: (0 is stop, 1 is play)", player.is_playing())
    return player.is_playing() != 0

def pause_music():
    print('pausing')
    player.set_pause(1)
    #Speak('Pausing')
    global ISPAUSED
    ISPAUSED = True

def resume_music():
    print('reusming')
    player.set_pause(0)
    #Speak('resuming..')
    global ISPAUSED
    ISPAUSED = False

def stop_music():

    print('stopping:::   ')
    #mixer.music.stop()
    player.stop()

def testing():
    #Speak('hi babyy can you give me achu plsss')
    # play_music(input('YOU:: '))
    # sleep(5)
    # pause_music()
    init_music()
    play_music('play dancing in the flames')
    print(music_is_playing())
    # print(find_playlist_name_in('jarvis play Dancing in the flames'))
    # print(song_is_downloaded('Dancing in the flames'))
    # importing vlc module
    # import required module
    # song_path = song_is_downloaded('Rap God')[1]

