#!/usr/bin/env python3

import subprocess as sp
import tkinter as tk 
from signal import pause
from pynput.keyboard import Listener
import asyncio

ITALIAN = "./data/video_italian.mp4"
ENGLISH = "./data/video_english.mp4"
LANGS = [ITALIAN, ENGLISH]

COMMAND = "mplayer -fs {} &"

def choose_video(index):
    return COMMAND.format(LANGS[index])

key = 'q'    

def on_press(key):
    if getattr(key, "char", None) == 'q':
        asyncio.run(run(choose_video(0)))
    elif getattr(key, "char", None) == 'w':
        asyncio.run(run(choose_video(1)))
    else:
        print(key)

listener = Listener(on_press=on_press, on_release=None)
listener.start()

root = tk.Tk() 
root.configure(bg='black', cursor='none')
root.attributes('-fullscreen', True)
root.update()

async def run(cmd):
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)

    await proc.communicate()

    print(f'[{cmd!r} exited with {proc.returncode}]')

pause()