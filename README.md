# MonroeAI 0.2

MonroeAI is skill based machine learning fueled text understanding library for chatbots somewhat like Amazon Alexa is. It can understand meaning from text (once trained), ask follow up questions and then execute code depending on that (e.g. query an API).

The understanding part of the library is done by giving text examples and then training a model. New
capabilities / skills can be added as plugins.

Note that this is still very much work in progress. 

### Features

Speech to text and random chatter capabilities removed as of 0.2 to renew the focus on plugin architecture.

  - Can add new skills as plugins
  - Uses machine learning to decide what the user wanted

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

This demonstrates the currency rate skill:

    You: Monroe please get me the exchange rate of USD
    Monroe: The exchange rate of USD against EUR is 1.1179 (source: European Central Bank, 2017-05-19)

This demonstrates the sleep mode skill:

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

You end the execution with an empty line

>Monroe: Or something
>You:
>No input. Bye!


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
