import azure.cognitiveservices.speech as speechsdk
import os
import time
import sys
import remi.gui as gui
from remi import start, App

speech_key, service_region = "e4e69d91801245bdbc350d3351db3238", "canadacentral"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)


class MyApp(App):
    def __init__(self, *args):
        super(MyApp, self).__init__(*args)

    def main(self):
        container = gui.VBox(width=1000, height=300)
        self.lbl = gui.Label('HTN Dyslexia')
        self.bt1 = gui.Button('Press to speak')
        self.bt2 = gui.Button('Press to stop')
        self.res = gui.Label('Look')

        # setting the listener for the onclick event of the button
        self.bt1.onclick.do(self.on_button_pressed1)
        self.bt2.onclick.do(self.on_button_pressed2)

        # appending a widget to another, the first argument is a string key
        container.append(self.lbl)
        container.append(self.bt1)
        container.append(self.bt2)
        container.append(self.res)

        # returning the root widget
        return container

    # listener function
    def on_button_pressed1(self, widget):
    # Copyright (c) Microsoft. All rights reserved.
    # Licensed under the MIT license. See LICENSE.md file in the project root for full license information.
    # Creates an instance of a speech config with specified subscription key and service region.
    # Replace with your own subscription key and service region (e.g., "westus").
    
    # speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

    # Creates a recognizer with the given settings
    # speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

        print("Say something...")
        result = ''
        def recognizing(evt):
            self.res.set_text(evt.result.text)
            print (evt.result.text)

        speech_recognizer.start_continuous_recognition()

        speech_recognizer.recognizing.connect(recognizing)
        #os.system('pause')
        

    def on_button_pressed2(self, widget):
        print("Terminated")
        speech_recognizer.stop_continuous_recognition()

# starts the web server
start(MyApp)


# def home():
#     return render_template('index.html')

# def speak():

#     # Copyright (c) Microsoft. All rights reserved.
#     # Licensed under the MIT license. See LICENSE.md file in the project root for full license information.
#     # Creates an instance of a speech config with specified subscription key and service region.
#     # Replace with your own subscription key and service region (e.g., "westus").
    
#     # speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

#     # Creates a recognizer with the given settings
#     # speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

#     print("Say something...")
#     result = ""
#     @app.route('/')
#     def recognizing(evt):
#         result = evt.result

#     speech_recognizer.start_continuous_recognition()

#     speech_recognizer.recognizing.connect(recognizing)
#     # os.system('pause')



# @app.route('/finished')
# def finished():
#     print("Terminated")
#     speech_recognizer.stop_continuous_recognition()

    

