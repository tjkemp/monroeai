"""Skillset tester. Creates a CLI to test skillset model's predictions. Enter a sentence
an see what function the sentence would map out to.

Usage: try_skillmodel.py MODEL

"""
from docopt import docopt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
import numpy
import pickle

def main():
	arguments = docopt(__doc__)

	filename_clf = arguments['MODEL'] + ".classifier.pkl"
	filename_vectorizer = arguments['MODEL'] + ".vectorizer.pkl"

	# load previously generated vectorizer and classifier
	with open(filename_vectorizer, 'rb') as f:
		vectorizer = pickle.load(f)
	with open(filename_clf, 'rb') as f:
		classifier = pickle.load(f)

	while (True):
		sentence = input(">>> ")

		if len(sentence) == 0:
			break

		predict_vector = vectorizer.transform([sentence])

		prediction = classifier.predict(predict_vector)
		print(prediction)

if __name__ == '__main__': 	main()
