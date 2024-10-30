import speech_recognition as sr
global recognizer, mic
recognizer = sr.Recognizer()
mic = sr.Microphone()  #Check the default microphone before getting to raspberry pi - sr.Microphone.list_microphone_names()

while True:
	with mic as source:
			try:
				recognizer.adjust_for_ambient_noise(source, 1.5)
				audio = recognizer.listen(source)
				text = recognizer.recognize_google(audio)
				print(text)
			except Exception as exp:
				print("Error occuured", exp.args)
