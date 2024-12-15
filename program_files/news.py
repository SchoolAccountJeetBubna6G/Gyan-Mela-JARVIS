# importing requests package
import requests	 

def Speak(text):
    import pyttsx3
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def news():
	print('news')
	query_params = {
    "source": "bbc-news",
	"sortBy": "top",
	"apiKey": "50df88c3d7c64804bb1d09628d62cc75"
    }
	main_url = "https://newsapi.org/v1/articles"
	res = requests.get(main_url, params=query_params)
	open_bbc_page = res.json()
	article = open_bbc_page["articles"]
	results = []
	for ar in article:
		results.append(ar["title"])
	Speak("Sure! The news for today are:")
	Speak(results)