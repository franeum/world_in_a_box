#!/usr/bin/env python3

import sys
import time
import tkinter as tk 
import RPi.GPIO as GPIO
import signal
#from mplayer import Player
from mpv import MPV
from gpiozero import Button

# GLOBAL LABELS

MAINPATH = "/home/neum/Documenti/world_in_a_box"
ITALIAN = f"{MAINPATH}/data/video_italian.mp4"
ENGLISH = f"{MAINPATH}/data/video_english.mp4"
LANGS = [ITALIAN, ENGLISH]
PUSH1 = 23
PUSH2 = 24
PUSH3 = 2
PUSH3PRESSED = Button(PUSH3, hold_time=1)

GPIO.setmode(GPIO.BCM)
GPIO.setup(PUSH1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(PUSH2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(PUSH3, GPIO.IN) 

class Video():
    def __init__(self):
        self.video = MPV()
        #self.is_playing = False

    def set_path(self, path):
        self.path = path

    def play(self):
        #self.is_playing = True
        self.video.play(self.path)

    def toggle_pause(self):
        #self.is_playing = not self.is_playing
        self.video.pause = not self.video.pause

VIDEO = Video()

def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)


def runvideo(push):
    index = 0 if push == 23 else 1
    lang = LANGS[index]

    for push in [PUSH1, PUSH2]:
        GPIO.remove_event_detect(push)
    
    VIDEO.set_path(lang)
    VIDEO.play()

def draw_bg():
  root = tk.Tk() 
  root.configure(bg='black', cursor='none')
  root.attributes('-fullscreen', True)
  root.update()

def togglevideo(push):
    VIDEO.toggle_pause()


def app_exit(push):
    sys.exit(0)


if __name__ == '__main__':
    GPIO.add_event_detect(PUSH1, GPIO.RISING, 
                callback=runvideo, bouncetime=400)
                
    GPIO.add_event_detect(PUSH2, GPIO.RISING, 
                callback=runvideo, bouncetime=400)

    #GPIO.add_event_detect(PUSH3, GPIO.RISING, 
                #callback=togglevideo, bouncetime=400)
                
    draw_bg()
    
    PUSH3PRESSED.when_released = togglevideo
    PUSH3PRESSED.when_held = app_exit

    signal.signal(signal.SIGINT, signal_handler)
    signal.pause()
