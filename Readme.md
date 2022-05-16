# Personal Voice Assistant

## What is Personal Voice Assistant ?
Virtual assistants like these can do everything from answer questions, tell jokes, play music, and control items in your home such as lights, thermostats, door locks, and smart home devices. They can respond to many voice commands, send text messages, make phone calls, and set up reminders. Anything you do on your phone, you can probably ask your virtual assistant to do for you. 

The virtual assistant must be connected to the internet so it can conduct web searches and find answers or communicate with other smart devices. However, since they're passive listening devices, they usually need a wake word or command to activate. That said, it's not unheard of that the device could start recording without a wake word. 

Basically, dialog systems use NLP to analyze speech in text form and to understand the user’s concern (intent). After the intentions have been recognized, the required action is carried out via the underlying API connections and returned to the user as feedback. The NLP is always based on text in different languages. For the conversion of spoken language, TTS (text to speech) engines are used, which generate text from speech that can be used by NLP. Either text is used for output or the text is converted back into spoken language using the STT (speech to text) engine.

## Why did I create this project ?

The aim of this project is to create a personal voice assistant which will be able to listen to the voice and act accordingly. For recognition of the voice or what the user said, a python library called SpeechRecognition will be used. And for deciding what to do from what the program hears, we will create a machine learning model which will decide what to do. To train the machine learning model, we will use a custom self-made dataset which will have text and intent, we will also create a function which will get the most related task if it is not given exact. We will also use some APIs for getting information, location, etc. We will use pvporcupine for detecting if a wake word (A word that will run the program).



## How to run ?

### Activate/Create the virtual environment 

#### Linux / Mac
```
python3 -m virtualenv venv
source venv/bin/activate
```
#### Windows
```
python -m virtualenv venv
.\venv\Scripts\activate.bat
```

### Install the Requirements
```
python -m pip install -r requirements.txt
```
### Run the program
```
python main.py
```