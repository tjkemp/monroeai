import speech_recognition as sr
import google_speech

SR_LANGS = {'fi': 'fi-FI',
	'en': 'en-US'}

def listen(lang):
	r = sr.Recognizer()
	with sr.Microphone() as source:
		audio = r.listen(source)
	try:
		# language in the format of fi-FI or en-US
		text = r.recognize_google(audio, language=SR_LANGS[lang])
		return text
	except sr.UnknownValueError:
		print("Google doesn't understand you")
	except sr.RequestError as e:
		print("Could not request results; {0}".format(e))

def speak(text, language):
	g = google_speech.Speech(text + " m", language)
	g.play(None)
