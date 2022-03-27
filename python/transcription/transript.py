from time import sleep
import azure.cognitiveservices.speech as speechsdk
import sys
import signal

sys.path.insert(0, '../')
sys.path.insert(0, '../interpret-blob')
sys.path.insert(0, '../TextAnalysis')
from conf import *
from blob import *
from analyse import *

speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, language="fr-FR")

res = []

def signal_handler(sig, frame):
    global res
    print("Cancelling program")
    speech_recognizer.stop_continuous_recognition()
    print("result res: " + res)
    print("replacing")
    print(res)
    analyse_input(res)
    exit()
    

signal.signal(signal.SIGINT, signal_handler)

def onRecognizing(e):
    print(e.result.text)
    global res
    res = e.result.text

def onRecognized(e):
    global res
    res.append(e.result.text)


'''speech_recognizer.recognizing.connect(onRecognizing)
#speech_recognizer.canceled.connect(onCancel)
result = speech_recognizer.start_continuous_recognition()
print("Begin Transcription !")
while True:
    sleep(0.5)'''