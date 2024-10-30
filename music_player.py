from noris_speak import Speak
from pygame import mixer
import random
import os
#STEPS TO GET MUSIC
"""
PRE-SETUP
1) Start program
2) Get songs in spotify playlists
3) Compare with the downloaded songs
4) If songs are there in spotify, which are no there in downloaded, download songs
6) Get the playlist that needs to be played - if none provided, play rap songs new
"""
#STEP TO DOWNLOAD MUSIC
"""
1) Use YT api, for the videos not in downloaded set, to get their URL
2) Use pytube to download videos
"""
#MAIN LOOP IF THIS IS CALLED
"""
1) Get the current playing song
2) If 'play' play, if 'stop' stop
3) If 'play' followed by a name (Determi`ne by some algorithm), play name
"""
CLIENT_ID = 'e20c25956b1e48228ddc9309f3e4d6b2'
CLIENT_SECRET = '27b5ee6d34d146e4b62ca13c9be25d42'
AUTOHORIZE_ENDPOINT = 'https://accounts.spotify.com/authorize'
REDIRECT_URL = "https://www.google.co.in/"
SCOPE = "user-read-playback-state user-modify-playback-state user-read-currently-playing app-remote-control streaming playlist-read-private playlist-modify-private playlist-modify-public user-follow-modify user-follow-read user-library-modify user-library-read user-read-email user-read-private user-read-playback-state user-modify-playback-state"
DEFAULT = r'C:\Users\Jeet\Desktop\Projects\PythonProjects\SpeechRecognition\Hitler Mk2 - Noris\Songs_downloaded\playlists\Rap Songs New'
PLAYLIST_PATH = r'C:\Users\Jeet\Desktop\Projects\PythonProjects\SpeechRecognition\Hitler Mk2 - Noris\Songs_downloaded\playlists'

PLAY_WORDS_NOT_REQ = ['play','blast'] #Words that if present, good, but if not, then its ok
COMMON_WORDS_COMPLEMENTS = ['please']
REQUIRED_WORDS = ['music', 'song']
IS_PLAYING = False
IS_PAUSED = False
SONGS = []
"""
def get_songs_in_spotify() -> list:
    
    def get_current_url(url:str) -> str:
        pass

    def get_code_spotify() -> str:
        import webbrowser
        from urllib.parse import urlencode

        auth_headers = {
            "client_id": CLIENT_ID,
            "response_type": "code",
            "redirect_uri": REDIRECT_URL,
            "scope": SCOPE
        }

        #webbrowser.open("https://accounts.spotify.com/authorize?" + urlencode(auth_headers))
        code_url = get_current_url("https://accounts.spotify.com/authorize?" + urlencode(auth_headers))
        #TO FINSIH NOT COMPLETE ------------------------  TO FINISH NOT COMPLETE        
    def get_access_code(code:str) -> str:
        pass

    code = get_code_spotify()
    access_code = get_access_code(code)
"""

"""
def check_if_downloaded():
    songs_spotify = get_songs_in_spotify()
    songs_downloaded = get_songs_downloaded()
    for song in songs_spotify:
        if song not in songs_downloaded:
            download_song(song)
"""

def download_song(song_name):
    from song_downloader import Download_song
    return Download_song(song_name)

def get_all_playlists_urls():
    global PLAYLIST_PATH
    folders_in_path = []
    folders_in_path =  [x[0] for x in os.walk(PLAYLIST_PATH)]
    #folders_in_path = [i.split('\\')[-1] for i in folders_in_path]
    return folders_in_path[1:]

def get_current_playing_song() -> str:
    pass

def get_playlist_url(text:str) -> str:
    playlists = get_all_playlists_urls()
    print('PLAYLISTS LINE 140 -', playlists)
    for playlist in playlists:
        if playlist in text:
            return playlist
    return ''


def get_songs_downloaded() -> list:
    pass

def get_song_name(text:str) -> str:
    text = text.split(' ')
    song_name = ''
    _ = []
    for index in range(len(text)):
        word = text[index]
        if word in PLAY_WORDS_NOT_REQ:
        #checks for some certain words
            _ = text[index+1:]
    for word_not_required in COMMON_WORDS_COMPLEMENTS:
        for word in _:
            if word == word_not_required:
                _.remove(word)

    song_name = ' '.join(_)
    return song_name


def get_songs_in_playlist(playlist_url:str) -> list:
        from os import listdir
        from os.path import isfile, join
        music_files = [f for f in listdir(playlist_url) if isfile(join(playlist_url, f))] #gets the files from the url
        print(music_files)
        return music_files


def Isplaylist(text:str) -> bool:
    """
    default = Rap songs new
    play music -> default
    play {music name} -> {music_name}
    """
    if 'music' not in text:
        return False
    else:
        return True

def load_songs():
    global SONGS
    import json
    with open('song_info.json', 'r') as file:
        SONGS = json.load(file)    

def pause_music():
    mixer.music.pause()
    Speak('pausing')
    global IS_PAUSED
    IS_PAUSED = True
    """ global IS_PLAYING
    IS_PLAYING = False """
    print('THE STATUS OF THE MIXER IS ', mixer.music.get_busy())


def play(music_files:list = [], APPROX_TIME_TO_RUN_LOOP:float = 0.001, volume:float = 0.3, song_name:str = '', text:str = '', playlist_url:str = '', is_playlist:bool = True):
    if is_playlist:
        import time
        random.shuffle(music_files) #Shuffle the playlist
        for music_file in music_files:
            play_function_bare(playlist_url+'/'+music_file, volume)
            _ = True
            while _:
                status = mixer.music.get_busy()
                if status == False and IS_PAUSED == False:
                    print('status and is_paused are negative ')
                    _ = False
    else:
        #Not playlist, a song.N
        #STEPS
        """
        1) Get the song name
        2) Search youtube for that song
        """
        if is_playlist == False and len(music_files) == 1:
            music_file = music_files[0]
            print('REACHED THE PLAY FUCNTION, MUSIC FILE IS',music_file)
            play_function_bare(music_file_path=music_file, volume=volume)

def play_function_bare(music_file_path, volume:0.3):
    mixer.init()
    mixer.music.load(music_file_path)
    mixer.music.set_volume(volume)
    mixer.music.play()

def play_music(text:str):
    #PRE SETUP 
    #check_if_downloaded()
    if len(SONGS) == 0:
        load_songs()
        print('LOADING SONGS......')
    is_playlist = Isplaylist(text)
    print('Is playlist...',is_playlist)
    if is_playlist:
        playlist_url = get_playlist_url(text)
        if playlist_url == '':
            print('playlist url is empty, try again')
            playlist_url = DEFAULT
        print('playlist_url',playlist_url)
        for word in REQUIRED_WORDS:
            if word in text:
                Speak('Sure! Playing music!')
                print('Playing, music!')
                #print(IS_PLAYING)
                global IS_PLAYING
                IS_PLAYING = True
                play(music_files=get_songs_in_playlist(playlist_url), APPROX_TIME_TO_RUN_LOOP=0.001, volume=0.4, song_name='',text=text, playlist_url=playlist_url, is_playlist=is_playlist)
        IS_PLAYING = False
    else:
        print('NOT A PLAYLIST!')
        song_name = get_song_name(text).lower()
        print('THE NAME OF THE SONG IS', song_name)
        IS_PLAYING = True
        #loop over all playlists to see if the song is there
        ##### WINDOWS DEPENDENT
        for song_info in SONGS:
            name = song_info['song name'].lower()
            if song_name == name:
                print(song_name)
                play(music_files=[song_info['file location']], is_playlist = False)
        else:
            song_path = download_song(song_name=song_name)
            play_function_bare(song_path, 0.3)
        IS_PLAYING = False

def unpause_muisc():
    mixer.music.unpause()
    Speak('unpausing')
    global IS_PAUSED
    IS_PAUSED = True
    global IS_PLAYING
    IS_PLAYING = True
    print('THE STATUS OF THE MIXER IS ', mixer.music.get_busy())

def stop_music():
    mixer.music.stop()
    Speak('stopping')        
    global IS_PLAYING
    IS_PLAYING = False
    print('THE STATUS OF THE MIXER IS ', mixer.music.get_busy())

#play_music('play music')