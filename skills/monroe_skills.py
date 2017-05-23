import random
import requests
import json

# called to greet the human when AI is first started
def greeting():
	replies = ["Hello!", "I'm here!", "How are you?"]
	return random.choice(replies), {}

# called to announce a skill is coming up
def attention_call():
	replies = ["Command me.", "How can I help you?", "What can I do for you?", "Your wish is my command."]
	return random.choice(replies), {'expecting_skill': True}

# called when AI asked to sleep
def go_to_sleep():
	replies = ["Good bye!", "I'm feeling sleepy.", "Bye bye!"]
	return random.choice(replies), {'awake': False}

# called when AI asked to wake up
def wake_up():
	replies = ["Good morning!", "I'm alive!", "Hello, nice to see you again!"]
	return random.choice(replies), {'awake': True}

def who_are_you():
	replies = ["I'm a PC.", "Who's asking?", "I'm your personal assistant."]
	return random.choice(replies), {}

# a fallback not to force a skill to be run when no skill matches the command
def undefined():
	return "I'm sorry, I don't understand.", {}

def tell_a_joke():
	replies = ["I don't know any jokes.", "Knock knock!"]
	return random.choice(replies), {}

# a function to retrieve the current exchange rate of USD against EUR
def exchange_rate():
	url = "http://api.fixer.io/latest?symbols=USD"
	headers = {'Accept': 'application/json'}

	r = requests.get(url, headers=headers)
	body = r.json()
	rate = body['rates']['USD']
	date = body['date']

	s = "The exchange rate of USD against EUR is {r} (source: European Central Bank, {d})".format(r=rate, d=date)
	return s, {}
