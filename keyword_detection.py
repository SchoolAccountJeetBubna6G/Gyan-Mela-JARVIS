def keyword_has_been_said_in(time:int) -> bool:
    return True ##FOR NOW

def hotword_in(text:str, words:list):
    try:
        text = text.split()
        #print('HOTWORD detected')
        print('keyword status:', any(x in text for x in words))
        return any(x in text for x in words)
    except Exception:
        #print('ERROR OCCURED IN KEYWORD DETECTION')
        pass