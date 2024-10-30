PATH_TO_SAVE = r"C:\Users\Jeet\Desktop\Projects\PythonProjects\SpeechRecognition\Hitler Mk2 - Noris\Songs_downloaded\Songs_independent"

def download(url, song):
    import yt_dlp
    global PATH_TO_SAVE                                                     #comment starts here, just test
    with yt_dlp.YoutubeDL( { 'extract_audio': True,  'format': 'bestaudio' """,  'outtmpl': PATH_TO_SAVE + '\\' + f'{song}.mp3' """} ) as video:
        info_dict = video.extract_info(url, download = True)
        video_title = info_dict['title']
        print(video_title)
        video.download(url)
        print("Successfully Downloaded - see local folder on Google Colab")


def getVidID(song):
    from youtubesearchpython import VideosSearch
    videosSearch = VideosSearch(f'{song} lyrics', limit = 2)
    return videosSearch.result()['result'][0]['id']


def Download_song(song):
    print("Downloading " + song)
    vidID = getVidID(song)
    link = 'https://www.youtube.com/watch?v=' + vidID
    download(link, song)
    print("Downloaded " + song + "\n")
    song_path = PATH_TO_SAVE + '\\' + f'{song}.mp3'
    return song_path

#Download_song('loose yourself')