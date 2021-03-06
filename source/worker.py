#!/usr/bin/env python3

import re
import sys
import signal
import tkinter as tk
import RPi.GPIO as GPIO
from pathlib import Path
from gpiozero import Button
from wab_video import Video
import wab_bg as background

# GLOBAL LABELS

MAINPATH = Path(__file__).parent.absolute()
VIDEO_DIR = (MAINPATH / '../VIDEO').resolve()
PATTERN = re.compile(r'^[12]_')
VIDEOS = [x for x in VIDEO_DIR.iterdir() if re.match(PATTERN, x.stem)]
PUSH1 = 23
PUSH2 = 24
PUSH3 = 25
PUSH3PRESSED = Button(PUSH3, hold_time=1)
VIDEO = Video()


def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)


def runvideo(push):
    # 0 if push == 23, otherwise 1 (for push 24)
    lang = VIDEOS[push - PUSH1]
    GPIO.setmode(GPIO.BCM)

    remove_event([PUSH1, PUSH2])

    VIDEO.set_path(lang)
    VIDEO.play()


def togglevideo(push):
    print("TOGGLE PAUSE")
    VIDEO.toggle_pause()


def app_exit(push):
    sys.exit(0)


def add_event(pushes):
    for push in pushes:
        GPIO.add_event_detect(push, GPIO.RISING,
                              callback=runvideo, bouncetime=400)


def remove_event(pushes):
    for push in pushes:
        GPIO.remove_event_detect(push)


VIDEO.set_callback(add_event, PUSH1, PUSH2)

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PUSH1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(PUSH2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    add_event([PUSH1, PUSH2])

    background.draw_bg()

    PUSH3PRESSED.when_released = togglevideo
    PUSH3PRESSED.when_held = app_exit

    signal.signal(signal.SIGINT, signal_handler)
    signal.pause()
