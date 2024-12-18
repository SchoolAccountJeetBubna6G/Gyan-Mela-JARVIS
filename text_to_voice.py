import os
import pygame
import random

def Speak(data):
    voice = 'en-US-JennyNeural'
    file_path = rf"C:\Users\Dell\Desktop\JEET\JarvisRefactored\voice_segments\{random.randint(100000,999999)}.mp3"
    command = f'edge-tts --voice "{voice}" --text "{data}" --write-media "{file_path}"'
    os.system(command)

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)

    try:
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except Exception as e:
        print(e)
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()


