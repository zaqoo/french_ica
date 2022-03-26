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
from translate import *

speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, language="fr-FR")

res = []
tmp = ""

def signal_handler(sig, frame):
    global res
    global tmp
    #res.append(tmp)
    print("Cancelling program")
    speech_recognizer.stop_continuous_recognition()
    print("result res: ")
    print(res)
    #print("replacing")
    #res = process_input(res)
    #print(res)
    str = translateText(' '.join(res))
    print('Translated : ' + str)
    analyse_input([str])
    exit()
    

signal.signal(signal.SIGINT, signal_handler)

def onRecognizing(e):
    print(e.result.text)
    global tmp
    tmp = e.result.text

def onReconnected(e):
    global res
    print("RECOOOOO")
    res.append(e.result.text)

speech_recognizer.recognizing.connect(onRecognizing)
speech_recognizer.recognized.connect(onReconnected)
#speech_recognizer.canceled.connect(onCancel)
result = speech_recognizer.start_continuous_recognition()
print("Begin Transcription !")
while True:
    sleep(0.5)