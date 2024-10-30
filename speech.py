def __init__(path_to_model:str, method:str='google'):
    if method == 'vosk':
        from vosk import KaldiRecognizer, Model
        import pyaudio
        global model_vosk, recognizer_vosk, stream_vosk

        model_vosk = Model(path_to_model)
        recognizer_vosk = KaldiRecognizer(model_vosk, 16000)
        mic_vosk = pyaudio.PyAudio()
        stream_vosk = mic_vosk.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)

    if method == 'google':
        import speech_recognition as sr
        global recognizer, mic
        recognizer = sr.Recognizer()
        mic = sr.Microphone()  #Check the default microphone before getting to raspberry pi - sr.Microphone.list_microphone_names()

def generate_text_vosk() -> str:
    stream_vosk.start_stream()
    data = stream_vosk.read(4096, exception_on_overflow=False)

    if recognizer.AcceptWaveform(data):
        text = recognizer.Result()
        return text[14:-3]

def generate_text_google() -> str:
    with mic as source:
        try:
            recognizer.adjust_for_ambient_noise(source, 0.6)
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            return text
        except Exception:
            print("Error occuured")
     
