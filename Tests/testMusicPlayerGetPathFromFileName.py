def testMusicPlayerGetPathFromFileName():
    playlist_url = 'Rap Songs New'
    from os import listdir
    from os.path import isfile, join
    music_files = [f for f in listdir(playlist_url) if isfile(join(playlist_url, f))] #gets the files from the url
    

testMusicPlayerGetPathFromFileName()