from flask import Flask
from time import sleep

import azure.cognitiveservices.speech as speechsdk
import sys
import signal
sys.path.insert(0, './')
sys.path.insert(0, './transcription')
sys.path.insert(0, './interpret-blob')
sys.path.insert(0, './TextAnalysis')
from time import sleep
from blob import *
from analyse import *
from conf import *
from transript import *
from translate import *

app = Flask(__name__)

speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, language="fr-FR")

@app.route('/')
def super_endpoint():
    speech_recognizer.recognized.connect(onRecognized)
    #speech_recognizer.canceled.connect(onCancel)
    result = speech_recognizer.start_continuous_recognition()
    print("Begin Transcription !")
    while True:
        sleep(0.5)


@app.route('/end')
def process_endpoint():
    global res
    print("Cancelling program")
    speech_recognizer.stop_continuous_recognition()
    print("result res: ")
    print(res)
    res = translateText(' '.join(res))
    print(res)
    analyse_input([res])
    exit()
