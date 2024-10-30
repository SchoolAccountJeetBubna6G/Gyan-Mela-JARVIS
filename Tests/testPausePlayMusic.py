from pygame import mixer
from time import sleep

files = ['Ballin.mp3', "Can't Be Touched.mp3", 'Cinderella Man.mp3', 'Doja.mp3', 'Fast Lane.mp3', 'Gnat.mp3', 'Go To Sleep.mp3', 'Godzilla.mp3', 'Higher.mp3', 'Homicide.mp3', 'Kamikaze.mp3', 'Killshot.mp3', 'Kings Never Die.mp3', 'Lose Yourself.mp3', 'Never Enough.mp3', 'Not Afraid.mp3', 'Remember the Name.mp3', 'Still D.R.E.mp3', 'The Monster.mp3', 'The Next Episode.mp3', 'The Real Slim Shady.mp3', 'Till I Collapse.mp3', 'Venom - Music From The Motion Picture.mp3', 'Welcome 2 Detroit.mp3', 'Where The Hood At.mp3']

def play_music(file):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    print('Playing music-------')

def pause_music():
    mixer.music.pause()
    print('Pausing music------')

def unpause_music():
    mixer.music.unpause()
    print('unpausing music------')

def stop_music():
    mixer.music.stop()
    print('Stopping music------')

def test(text):
    for song in files:
        play_music(r'C:\Users\Jeet\Desktop\Projects\PythonProjects\SpeechRecognition\Hitler Mk2 - Noris\Songs_downloaded\playlists\Rap Songs New'+f'\{song}')


def get_songs_in_playlist(playlist_url:str) -> list:
        from os import listdir
        from os.path import isfile, join
        music_files = [f for f in listdir(playlist_url) if isfile(join(playlist_url, f))] #gets the files from the url
        print(music_files)
        return music_files

#get_songs_in_playlist(r'C:\Users\Jeet\Desktop\Projects\PythonProjects\SpeechRecognition\Hitler Mk2 - Noris\Songs_downloaded\playlists\Rap Songs New')
test()