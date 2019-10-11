# Controlling your mouse
# listening to your mouse
# controlling your keyboard
# listening to your keyboard - will be finally usd in our keylogger

from pynput.mouse import Controller
from pynput.keyboard import Controller


# Function for Controlling your mouse
def controlmouse():
    mouse = Controller()
    mouse.position = (40, 40)


# Function for controlling your keyboard
def controlkeyboard():
    keyboard = Controller()
    keyboard.type('I am learning to control keyboard')


controlkeyboard()
