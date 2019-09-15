import azure.cognitiveservices.speech as speechsdk
import os
import time
import sys
import remi.gui as gui
from remi import start, App
import numpy as np

speech_key, service_region = "Enter_key_here", "canadacentral"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

class MyApp(App):
    def __init__(self, *args):
        super(MyApp, self).__init__(*args)

    def main(self):

        for line in f:
            self.paragraph = gui.Label(line)
            break
            
        container = gui.VBox(width=1000, height=300)
        self.lbl = gui.Label('Say the following:')
        self.bt1 = gui.Button('Press to speak')
        self.bt2 = gui.Button('Press to stop')  
        self.res = gui.Label('Look')
        self.incorrectNum = gui.Label("Incorrect: ")

        # setting the listener for the onclick event of the button
        self.bt1.onclick.do(self.on_button_pressed1)
        self.bt2.onclick.do(self.on_button_pressed2)

        # appending a widget to another, the first argument is a string key
        container.append(self.lbl)
        container.append(self.paragraph)
        container.append(self.bt1)
        container.append(self.bt2)
        container.append(self.res)
        container.append(self.incorrectNum)

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

        self.incorrectNum.set_text("You had: ")
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
        user_input = self.res.get_text()
        user_input_array = user_input.split()

        incorrect = 0
        # line = ""
        # for i in g:
        #     line = i
        #     break
        line = g.readline()

        words = line.split() 
        diff_size = abs(len(user_input_array) - len(words))
        if diff_size>0:
            for i in range(diff_size):
                user_input_array.append(None)
        
        print(words)
        print(user_input_array)
        
        common = len(list(set(words).intersection(user_input_array)))
        print(common)
        if len(words) - common == diff_size:
            incorrect = diff_size
        else:
            for i in range(len(words)):
                if words[i] != user_input_array[i]:
                    incorrect+=1

        incorrectString = str(incorrect)
        self.incorrectNum.set_text("You had: " + incorrectString + " Errors")
        

f = open(r'C:\Users\Piyush\Documents\GitHub\HTN2019\app\user.txt', 'r')
g = open(r'C:\Users\Piyush\Documents\GitHub\HTN2019\app\computerInfo.txt', 'r')
start(MyApp)
