# MonroeAI 0.1

MonroeAI is cloud-enabled digital assistant. This is still very much work in progress, but it works. It turns speech into text, then decides with a machine learning model whether a skill (eg. query some API for info etc) should be run or whether to fallback to a chatbot and generate some small talk.

It runs locally in a prompt and should work with Windows and Linux.

### Features

  - Speach-To-Text and Text-To-Speach
  - Can add new skills as plugins
  - Uses machine learning to decide what the user wanted
  - Falls back to chatter if no meaning was found

### An example conversation

Monroe: I'm here!
You: How are you?
Monroe: I'm good thank you
You: Good to hear
Monroe: How about you?
You: I'm fine, thanks for asking
Monroe: oh you'd like to ask me a question
You: You bet I do
Monroe: bye bye bye
You: How about that question?
Monroe: Go ahead and ask.
You: How much is the fish?
Monroe: What is it that you want to know?
You: Are you alive?
Monroe: Yes I am.
You: Monroe please get me the exchange rate of USD
Monroe: The exchange rate of USD against EUR is 1.1179 (source: European Central Bank, 2017-05-19)
You: Thanks!
Monroe: that's a very funny joke
You: Monroe
Monroe: How can I help you?
You: Go to sleep
Monroe: Good bye!
You: Are you there?
You: Hello?
You: Wake up
You: Monroe wake up
Monroe: Good morning!
You: Morning
Monroe: Or something
You: Bye
Monroe: Tell me
You:
No input. Bye!


## Installation

1. Install the dependencies.

```sh
$ cd MonroeAI
$ mkvirtualenv MonroeAI
$ pip install -r requirements.txt
```

2. Install PortAudio to be able to produce sound www.portaudio.com/download.html

## Running Monroe

Check config.yaml and change interface to "voice" if you want to run it with voice commands instead of running it in text mode ("cli"). You can also change the name of the AI with ainame parameter. The name is important as saying it or typing it as the first word of input will let the AI know that a skill is to be evoked.

Just run it
```sh
$ python3 monroe.py
```

## Plugins

Currently there are not very many plugin capabilities. Two plugins are querying fixer.io for USD exchange rates and going to sleep mode.

To create new plugin create a yaml file with sample utterances which activate skill (see other yaml-files in skill directory for examples) and add the skill as a function to monroe_skills.py.

After that update the skill model by running create_skillmodel.py

```sh
$ python3 create_skillmodel.py monroe_skills core_skills sleep_skills currency_skills
```

You can then try and see what sentences map to which sentences with try_skillmodel.py

```sh
$ python3 try_skillmodel.py monroe_skills
```

An example of testing the model:

```>>> How are you?
['wake_up']
>>> EUR to USD
['exchange_rate']
>>> go sleep
['go_to_sleep']
```
