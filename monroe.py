import sys
import yaml
import importlib
import pickle
from FrontLobe import brain, speech_google
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC


DEFAULT_CONFIG = "config.yaml"
SKILLS_DIR = "skills"

class Monroe(object):
	""" Monroe is a main loop of the AI. It takes care of initialization of AI and the
	interface. """

	def __init__(self, ainame, lang):
		self.ainame = ainame
		self.lang = lang

	def init_skills(self, skillset):
		""" Function to initialize AI skills. Variable 'skillset' defines the names of the 
		vectorizer, classifier and python modules files to be used. """

		# load module that includes the skills and the model which determines 
		# which function to fire with a given input
		module_name = SKILLS_DIR + "." + skillset
		skillmodule = importlib.import_module(module_name)

		modelpath = SKILLS_DIR + "/" + skillset
		with open(modelpath + '.vectorizer.pkl', 'rb') as f:
			vectorizer = pickle.load(f)
		with open(modelpath + '.classifier.pkl', 'rb') as f:
			classifier = pickle.load(f)
		
		self.AI = brain.Brain(self.ainame, self.lang, skillmodule, classifier, vectorizer)
		return

	def voice(self):
		""" Main loop if AI is run with voice interface. """

		listen = speech_google.listen
		speak = speech_google.speak

		text = self.AI.say_hello()

		self._speak(text, self.ainame)
		speak(text, self.lang)

		try:
			while True:
				text = listen(self.lang)
				if text is None or len(text) == 0:
					print("No input. Bye!")
					return
				self._speak(text, "You")
				answer = self.AI.think(text)

				self._speak(answer, self.ainame)
				speak(answer, self.lang)
		
		except KeyboardInterrupt:
			pass
		return

	def cli(self):
		""" Main loop if AI is run with command line interface. """
		text = self.AI.say_hello()
		self._speak(text, self.ainame)

		try:
			while True:
				text = self._listen()
				if text is None or len(text) == 0:
					print("No input. Bye!")
					return
				answer = self.AI.think(text)
				self._speak(answer, self.ainame)
		
		except KeyboardInterrupt:
			pass
		return

	def _listen(self):
		""" A function to get input from command line. Used when run in command-line mode. """
		text = input('You: ')
		return text

	def _speak(self, text, who=""):
		""" A function to output answers. Used when run in command-line mode. """
		if len(text) > 0:
			print(who + ": " + text)
		return

def main():
	# first read general configurations
	with open(DEFAULT_CONFIG, 'r') as f:
		conf = yaml.safe_load(f)

	ainame = conf["ainame"]
	lang = conf["lang"]
	skillset = conf["skillset"]
	iface = conf["interface"]

	# start the ai instance, set it's name and used language
	m = Monroe(ainame, lang)
	# initialize skills
	m.init_skills(skillset)
	print(iface)
	if iface == "voice":
		m.voice()
	else:
		m.cli()

if __name__ == '__main__': main()