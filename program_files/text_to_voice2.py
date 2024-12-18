import os
import pygame

def Speak(data):
    voice = 'en-US-JennyNeural'
    command = f'edge-tts --voice "{voice}" --text "{data}" --write-media "data1.mp3"'
    os.system(command)

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("data1.mp3")

    try:
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except Exception as e:
        print(e)
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()

