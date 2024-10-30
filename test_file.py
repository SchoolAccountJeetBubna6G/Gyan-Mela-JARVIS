import os
import json
SONGS = []
X = r'C:\Users\Jeet\Desktop\Projects\PythonProjects\SpeechRecognition\Hitler Mk2 - Noris\Songs_downloaded\playlists'
for playlist in os.listdir(X):
    for song in os.listdir(X +'\\' + playlist):
        SONGS.append({'song name':song[:-4], 'file location':X + '\\' + playlist + '\\' + song})
with open('song_info.json', 'r+') as file:
    json.dump(SONGS, fp=file, indent=2)
        

print(SONGS)