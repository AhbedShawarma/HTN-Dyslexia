from app import app
import azure.cognitiveservices.speech as speechsdk
import os
import time
import sys
from flask import render_template, jsonify, request

speech_key, service_region = "e4e69d91801245bdbc350d3351db3238", "canadacentral"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/speak')
def speak():

    # Copyright (c) Microsoft. All rights reserved.
    # Licensed under the MIT license. See LICENSE.md file in the project root for full license information.
    # Creates an instance of a speech config with specified subscription key and service region.
    # Replace with your own subscription key and service region (e.g., "westus").
    
    # speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

    # Creates a recognizer with the given settings
    # speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

    print("Say something...")

    def recognizing(evt):
        print(evt.result)

    speech_recognizer.start_continuous_recognition()

    speech_recognizer.recognizing.connect(recognizing)
    # os.system('pause')

@app.route('/finished')
def finished():
    print("Terminated")
    speech_recognizer.stop_continuous_recognition()
    

