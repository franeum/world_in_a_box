#!/usr/bin/env python3

import tkinter as tk
from pathlib import Path
from gpiozero import Button
#from mplayer import Player

BLACKPIN = 2
BLACKPUSH = Button(BLACKPIN)

class Background:
    def __init__(self):
        self.active = False
        self.draw()

    def draw(self):
        if not self.active:
            self.win = tk.Tk()
            self.active = True
        
        self.win.configure(bg='black', cursor='none')
        self.win.attributes('-fullscreen', True)
        self.win.update()

    def destroy(self):
        self.active = False
        self.win.destroy()

WINDOW = Background()

def g_exit():
    if WINDOW.active:
        WINDOW.destroy()
    else:
        WINDOW.draw()

if __name__ == "__main__":
    BLACKPUSH.when_held = g_exit