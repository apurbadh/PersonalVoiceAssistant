import pvporcupine
import pyaudio
from assistant_functions.speak_listen import speak_listen
from intentclassification.intent_classification import IntentClassifier
from assistant_functions.reply import reply
from assistant_functions.weather import weather
from assistant_functions.location import location
from assistant_functions.open_browser import assistant_browser
import struct

class PersonalAssistant:

    def __init__(self, name):
        self.name = name
        
    
    def reply(self, text):
        intent = intentclassifier.predict(text)
        
        replies = {
            'leaving' : reply,
            'greeting' : reply,
            'insult' : reply,
            'personal_q' : reply,
            'weather' : weather.main,
            'location' : location.main,
            'open_in_browser':assistant_browser.main,
            }

        reply_func = replies[intent]

        if callable(reply_func):
            reply_func(text, intent)

    def run(self):
        self.porcupine = None
        pa = None
        audio_stream = None


        self.porcupine = pvporcupine.create(keywords=["picovoice"], access_key='BnM96C++XimpSouEsKUe4rU3RshuqFejt5YJqLC4AZthUVsrJ0Twmw==')

        pa = pyaudio.PyAudio()

        audio_stream = pa.open(
                        rate=self.porcupine.sample_rate,
                        channels=1,
                        format=pyaudio.paInt16,
                        input=True,
                        frames_per_buffer=self.porcupine.frame_length)
        
        while True:
            try: 
                pcm = audio_stream.read(self.porcupine.frame_length)
                pcm = struct.unpack_from("h" * self.porcupine.frame_length, pcm)
            except:
                audio_stream = pa.open(
                    rate=self.porcupine.sample_rate,
                    channels=1,
                    format=pyaudio.paInt16,
                    input=True,
                    frames_per_buffer=self.porcupine.frame_length)

            keyword_index = self.porcupine.process(pcm)

            if keyword_index >= 0:
                print("Hotword Detected")
                
 

                if audio_stream is not None:
                     audio_stream.close()
                said = speak_listen.listen()
                print(said)


                self.reply(said)
    
                
    

if __name__ == "__main__":
    intentclassifier = IntentClassifier()
    assistant = PersonalAssistant("Assistant")
    assistant.run()