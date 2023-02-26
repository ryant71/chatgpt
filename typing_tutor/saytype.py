#!/usr/bin/env python3

import random
import pyttsx3

# initialize the text-to-speech engine
engine = pyttsx3.init()

# function to speak a random letter
def speak_letter():
    # generate a random letter
    letter = chr(random.randint(65, 90))
    # speak the letter
    engine.say(letter)
    engine.runAndWait()
    return letter

# loop until the user interrupts the script
while True:
    # speak a random letter
    letter = speak_letter()
    # prompt the user to type the letter
    response = input("Type the letter: ")
    # check if the response is correct
    if response.upper() == letter:
        engine.say("correct")
        engine.runAndWait()
    else:
        engine.say("Ehhh, try again")
        engine.runAndWait()
