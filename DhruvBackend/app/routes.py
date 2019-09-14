from app import app
from flask import render_template, jsonify, request

global text

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/finished')
def finished():
    print ("HELLO")
    return ("Hello")

@app.route('/index')
def index():
    import time
    import os
# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE.md file in the project root for full license information.

    import azure.cognitiveservices.speech as speechsdk

# Creates an instance of a speech config with specified subscription key and service region.
# Replace with your own subscription key and service region (e.g., "westus").
    speech_key, service_region = "e4e69d91801245bdbc350d3351db3238", "canadacentral"

    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

# Creates a recognizer with the given settings
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

    print("Say something...")

    def recognizing(evt):
        print(evt.result)

    speech_recognizer.recognizing.connect(recognizing)
    speech_recognizer.start_continuous_recognition()

    os.system('pause')