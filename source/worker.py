#!/usr/bin/env python3

import re
import sys
import signal
import tkinter as tk
import RPi.GPIO as GPIO
from pathlib import Path
from gpiozero import Button
from wab_video import Video

# GLOBAL LABELS

MAINPATH = Path('.').resolve()
VIDEO_DIR = (MAINPATH / '../data').resolve()
PATTERN = re.compile(r'^[12]_')
VIDEOS = [x for x in VIDEO_DIR.iterdir() if re.match(PATTERN, x.stem)]
PUSH1 = 23
PUSH2 = 24
PUSH3 = 2
PUSH3PRESSED = Button(PUSH3, hold_time=1)

GPIO.setmode(GPIO.BCM)
GPIO.setup(PUSH1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(PUSH2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

VIDEO = Video()

def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)


def runvideo(push):
    # 0 if push == 23, otherwise 1 (for push 24)
    lang = VIDEOS[push - PUSH1]

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
                
    draw_bg()
    
    PUSH3PRESSED.when_released = togglevideo
    PUSH3PRESSED.when_held = app_exit

    signal.signal(signal.SIGINT, signal_handler)
    signal.pause()
