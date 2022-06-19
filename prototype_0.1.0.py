#!/usr/bin/env python3

import sys
import asyncio
#import subprocess as sp
import tkinter as tk 
import RPi.GPIO as GPIO
import signal

# GLOBAL LABELS

MAINPATH = "/home/neum/Documenti/world_in_a_box"
ITALIAN = f"{MAINPATH}/data/video_italian.mp4"
ENGLISH = f"{MAINPATH}/data/video_english.mp4"
LANGS = [ITALIAN, ENGLISH]
COMMAND = "pkill mplayer; mplayer -fs -ao alsa {} > /dev/null 2>&1 &"
PUSH1 = 23
PUSH2 = 24
#PUSH3 = 2

GPIO.setmode(GPIO.BCM)
GPIO.setup(PUSH1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(PUSH2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(PUSH3, GPIO.IN)


def signal_handler(sig, frame):
    #GPIO.cleanup()
    sys.exit(0)


def runvideo(push):
  index = 0 if push == 23 else 1
  lang = LANGS[index]
  asyncio.run(run(COMMAND.format(lang)))
  
    
async def run(cmd):
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)

    await proc.communicate()

    print(f'[{cmd!r} exited with {proc.returncode}]')
    
def draw_bg():
  root = tk.Tk() 
  root.configure(bg='black', cursor='none')
  root.attributes('-fullscreen', True)
  root.update()

if __name__ == '__main__':
  GPIO.add_event_detect(PUSH1, GPIO.RISING, 
              callback=runvideo, bouncetime=400)
              
  GPIO.add_event_detect(PUSH2, GPIO.RISING, 
              callback=runvideo, bouncetime=400)
              
  draw_bg()
  
  signal.signal(signal.SIGINT, signal_handler)
  signal.pause()
