import azure.cognitiveservices.speech as speechsdk
import sys
import signal
sys.path.insert(0, '../')
sys.path.insert(0, '../analyse_input')
from conf import *


def onRecognizedWord(e):
    print("Bonjour has been deteced")
    # call transcript method

def onCancel(e):
    print("Recognization has been stoped")


bonjourModel = speechsdk.KeywordRecognitionModel("173b1f0a-76b5-41d1-a626-c2ecade0b19a.table")
enRevoirModel = speechsdk.KeywordRecognitionModel("0b00ed3f-a7f3-4574-a666-1f471bda8e8c.table")

recognizer = speechsdk.KeywordRecognizer()
recognizer.recognized.connect(onRecognizedWord)
recognizer.canceled.connect(onCancel)

def signal_handler(sig, frame):
    print("Cancelling program")
    recognizer.stop_recognize_async()

signal.signal(signal.SIGINT, signal_handler)

result = recognizer.recognize_once_async(bonjourModel)
result.get()

#maybe check for result ?!


