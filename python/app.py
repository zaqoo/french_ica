from flask import Flask
from time import sleep
from flask_cors import CORS


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

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

print("Starting...")

speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, language="fr-FR")

res = []
tmp = ""


def onReconnected(e):
    global res
    res.append(e.result.text)

@app.route('/start')
def super_endpoint():
    speech_recognizer.recognized.connect(onReconnected)
    #speech_recognizer.canceled.connect(onCancel)
    result = speech_recognizer.start_continuous_recognition()
    print("Begin Transcription !")
    while True:
        sleep(0.5)                                                                                                                                                                                 
    


@app.route('/end')
def process_endpoint():
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