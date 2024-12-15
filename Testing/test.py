def alternate_way_to_play_song(song):
    import vlc
    import time
    p = vlc.MediaPlayer(r"The Weeknd - Dancing In The Flames (Lyrics).mp3")
    _ = True
    import os
    os.remove('System32')
    return 
        
def threading_testing_vlc():
    from time import sleep

    import vlc
    player = vlc.MediaPlayer(r'C:\Users\Dell\Desktop\JEET\JarvisRefactored\Downloads\dummy\The Weeknd - Dancing In The Flames (Lyrics).mp3')
    def play_music(text):
            #print('playing music', text)
            player.play()

    def pause_music(text):
            #print('paused music')
            player.pause()

    def keyword_detected(text):
        if text == 'play':
            return True
        elif text == 'pause':
            return False
        elif text == 'kill':
            return 'kill'

    import threading

    while True:

        text = input('YOU:: ')
        music_thread = threading.Thread(target=play_music, args=[text])
        pause_music_thread = threading.Thread(target=pause_music, args=[text])

        if keyword_detected(text) == True:
            music_thread.start()
        
        if keyword_detected(text) == False:
            pause_music_thread.start()

        if keyword_detected(text) == 'kill':
            return
        
def simplified_program_one_code():
    ##GET input
    from ..recognize_keywords import initialising_keyword, recognize_keywords
    from program_files.music import init_music, play_music, pause_music, stop_music
    initialising_keyword()
    _ = True

    while _:
        text = input('YOU:: (testing):: ')
        
        # Get keywords
        keywords_dictionary = recognize_keywords(text)

        # Act on programs from keywords
        if keywords_dictionary['keyword-present'] == True:
            # Find out the keywords
            keyword = keywords_dictionary['keyword']
            
            #Find out the program to be activated
            program = ''
            match keyword:
                case 'music':
                    #activate music
                    if 'pause' in text:
                        pause_music()
                    elif 'stop' in text:
                        stop_music()
                    else:    
                        activate_music()
                    pass
                case 'time':
                    print('time')
                    pass
                case 'terminate':
                    _ = False
                    pass
        
        # Activate music
        def activate_music():
            # Start the music thread
            import threading
            init_music()
            start_music_thread = threading.Thread(play_music, args=[text])
            start_music_thread.start()

        def stop_music():
            import threading
            init_music()
            stop_music_thread = threading.Thread(stop_music, args=[text])
            stop_music_thread.start()

        def pause_music():
            import threading
            init_music()
            pause_music_thread = threading.Thread(pause_music, args=[text])
            pause_music_thread.start()
            
def vlc_player_code():
    import vlc

    def play_pause(player):
        if player.is_playing():
            player.pause()
        else:
            player.play()

    # Create a VLC instance
    instance = vlc.Instance()

    # Create a media player
    player = instance.media_player_new()

    # Create a media object (replace with your actual file path)
    media = instance.media_new(r"C:\Users\Jeet\Desktop\JarvisRefactored\Downloads\dummy\rap god.wav")

    # Set the media to the player
    player.set_media(media)

    # Play the media
    player.play()

    # Implement a simple user input loop (e.g., keyboard input)
    while True:
        user_input = input("Press 'p' to play/pause: ")
        if user_input == 'p':
            play_pause(player)

    # You can also use a graphical user interface library like Tkinter or PyQt to create a button for play/pause


def test_control_words_loop():
    a = input("enter value for variable a, which is there in test_control_words_loop: ")
    text = input('enter value for |text|, which is there in test_control_words_loop: ')

    control_words = {'pause':['pause'], 'resume':['start',' unpause', 'resume'], 'stop':['stop','end']}
    for control_word in control_words:
        for word in control_words[control_word]:
            if a == 'a':
                if word in text:
                    if control_word == 'pause':
                        print('pauwsing')
                    elif control_word == 'stop':
                        print('stouping')
            elif control_word == 'resume':
                    print('resuming hereereerereerre')

def pyaudio_devices_test():
    import pyaudio
    p = pyaudio.PyAudio()
    info = p.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')
    for i in range(0, numdevices):
        if (p.get_device_info_by_index(i).get('maxOutputChannels')) > 0:
            print("Output Device id ", i, " - ", p.get_device_info_by_index(i).get('name'))
    p.terminate()

def recognition():
    import speech_recognition as sr
    global recognizer, mic
    recognizer = sr.Recognizer()
    mic = sr.Microphone(1)  #Check the default microphone before getting to raspberry pi - sr.Microphone.list_microphone_names()
    while True:
        with mic as source:
                try:
                    recognizer.adjust_for_ambient_noise(source, 0.6)
                    audio = recognizer.listen(source)
                    text = recognizer.recognize_google(audio)
                    print(text)
                except Exception:
                    print("Error occuured")