"""Trains a skillset model for Monroe AI. Creates a model and a vectorizer files 
using one more skill files.

Usage:
	create_skillmodel.py MODELNAME SKILL...
	create_skillmodel.py
Example:
	create_skillmodel.py monroe_skills core_skills sleep_skills currency_skills
Arguments:
	MODELNAME	name for the created skillset, it should match the python module name 
	SKILL		skill name, eg. "default"

"""
from docopt import docopt
import yaml
import pprint
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score

def load_skilldata(datasets=['base', 'chat']):
	sentences = []
	labels = []

	for ds in datasets:
		filename = ds + ".yaml"
		with open(filename, 'r') as f:
			skills = yaml.safe_load(f)
		for label in skills.keys():
			sentences += [s.strip() for s in skills[label]]
			labels += [label] * len(skills[label])
	return sentences, labels

def main():
	arguments = docopt(__doc__)
	print(arguments)
	filename_clf = arguments['MODELNAME'] + ".classifier.pkl"
	filename_vectorizer = arguments['MODELNAME'] + ".vectorizer.pkl"
	datasets = arguments['SKILL']
	# use skill yaml files to generate training data
	train_sentences, train_labels = load_skilldata(datasets)

	# convert sentences to feature vectors
	print ("Creating a vectorizer...")
	vectorizer = TfidfVectorizer(analyzer='word', norm='l2')
	vectorizer.fit(train_sentences)

	print ("Vectorizing training set...")
	train_vectors = vectorizer.transform(train_sentences).toarray()
	
	#test for the best classifier
	score_best = 0.0
	c_best = -1
	classifier_best = None

	print ("Evaluating the best hyperparameter C...")
	for i in range (-10, 10):
		c = 2**i
		classifier = LinearSVC(C=c)
		classifier.fit(train_vectors, train_labels)
		# OBS ! testing with training data
		score = accuracy_score(train_labels, classifier.predict(train_vectors))
		if score > score_best:
			c_best = c
			score_best = score
			classifier_best = classifier
		print ("With C = %s training set accuracy: %s." % (c, score))

	print ("Best C value is %s with the accuracy of %s." % (c_best,score_best))

	# save the best classifier
	print ("Saving vectorizer and classifier...")
	with open(filename_vectorizer, 'wb') as f:
	    pickle.dump(vectorizer, f, pickle.HIGHEST_PROTOCOL)
	with open(filename_clf, 'wb') as f:
	    pickle.dump(classifier_best, f, pickle.HIGHEST_PROTOCOL)
	print ("Done.")

if __name__ == '__main__': 	main()
