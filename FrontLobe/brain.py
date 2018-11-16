from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
import numpy as np

class Brain(object):
	""" Brain is the instance that processes text input and generates output. """

	def __init__(self, ainame, lang, skillmodule, classifier, vectorizer):
		self.ainame = ainame
		self.lang = lang
		self.skillmodule = skillmodule
		self.skill_classifier = classifier
		self.skill_vectorizer = vectorizer
		self.parameters = {
			'awake': True,
			'expecting_skill': False  }

	def say_hello(self):
		answer, params = getattr(self.skillmodule, "greeting")()
		return answer

	def think(self, speech_text):
		""" The method returns an answer by firing a skill function.
		Also it controls the awake/sleep status of the AI. """

		text = speech_text
		# if the name of the AI is found in text then we awaken sleeping AI and evoke a skill
		run_skill = False
		words = text.split()

		if self.ainame in words:
			run_skill = True
			self.parameters['awake'] = True

			# clean the name of AI from text in order to keep it separate
			words = [x for x in words if x != self.ainame]
			text = " ".join(words)

		# also a previous skill can have evoked an expectation of skill
		if self.parameters['expecting_skill'] is True:
			run_skill = True
			self.parameters['expecting_skill'] = False

		if (run_skill):
			answer, params = self._skill_answer(text)
			self.parameters = {**self.parameters, **params}
			return answer

		# as a fallback we use give an answer from chatterbot
		if self.parameters['awake'] is True:
			return self._chat_answer(text)
		return ""

	def _skill_answer(self, text):
		""" Scripted answer processses specific commands that are to activate specific function 
		or give a specific answer, compared to idle chat.  """
		if len(text.strip()) == 0:
			return getattr(self.skillmodule, "attention_call")()

		predict_vector = self.skill_vectorizer.transform([text])
		prediction = self.skill_classifier.predict(predict_vector)
		function = np.array_str(prediction[0])
		return getattr(self.skillmodule, function)()

	def _chat_answer(self, text):
		""" This function gives random chatter answer to input. """

		response = "Sorry, I don't understand"

		return response
