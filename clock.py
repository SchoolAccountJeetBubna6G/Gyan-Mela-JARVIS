import noris_speak as ns
#import pyttsx3 as speech
import keyword_filter
import conversion
from time import sleep

def create_timer(time_):
    time_val = time_
    print(f'Timer started ------------------------------------- timer time: {time_})')
    ns.Speak(f'Sure! Timer started for {time_}')
    while time_val > 0:
        time_val -= 1
        print('Time remaining:',time_val)
        sleep(1)
    print('Timer ended ------------------------------------')
    ns.Speak("Your timer is over...."*3)
    return
