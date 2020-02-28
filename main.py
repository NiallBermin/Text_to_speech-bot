import speech_recognition as sr
from code.Files import *
from code.Voice import *
from code.System_command import *
from code.config import *
from gtts import gTTS
import os


r = sr.Recognizer()
# Take input from the microphone and gives it the value of source
with sr.Microphone() as source:
    # Asks the user for input
    print("Hello and welcome to pyChat give me a command to run")
    talk("Hello " + name + " and welcome to pyChat give me a command to run", language)
    sentence = ""
    while ("exit" not in sentence) and ("goodbye" not in sentence):
        #listens to the microphpne
        audio = r.listen(source)
        # uses google speech recognition to tranlate to text and converts if no error has occured
        try:
            sentence = r.recognize_google(audio)
            print("TEXT: " + sentence)
        except:
            pass

        #run a system command trough the terminal
        if "system command" in sentence.lower():
            print("what command would you like to run?")
            talk("what command would you like to run?", language)
            audio = r.listen(source)
            while "cancel" != sentence:
                audio = r.listen(source)
                try:
                    sentence = r.recognize_google(audio)
                    print(sentence)
                    # runs command in terminal using the systemCommand function
                    if systemCommand(sentence, directory):
                        talk("have run command " + sentence, language)
                        sentence = "cancel"
                    else:
                        talk("failed to run the command " + sentence, language)
                except:
                    pass
        if ("read file" in sentence):
            doc = open("batman.txt", "r")
            lies = doc.read()
            doc.close()
            talk(lies, language)
        #edit an already existing file
        if ("edit file" in sentence):
            print("What file do you wish to edit?")
            talk("What file do you wish to edit", language)

            while "cancel" != sentence:
                audio = r.listen(source)
                try:
                    sentence = r.recognize_google(audio)
                    if sentence != "cancel":
                        talk(editFile(sentence, directory), language)
                        sentence = "cancel"
                    else:
                        talk("You have canceled editing a file", language)
                except:
                    print("tell me a filename")
        # checks for strings in sentence variable to call a command
        if ("open" or "create" in sentence) and ("new" in sentence) and ("file" in sentence):
            print("What do u want to call the new file?")
            talk("What do u want to call the new file?", language)

            while "cancel" != sentence:
                audio = r.listen(source)
                try:
                    sentence = r.recognize_google(audio)
                    if sentence != "cancel":
                        talk(newfile(sentence, directory), language)
                        sentence = "cancel"
                    else:
                        talk("You have canceled createing a new file", language)
                except:
                    print("tell me a filename")
    # just here to say goodbye
    print("Good bye for now")
    talk("Good bye for now", language)
