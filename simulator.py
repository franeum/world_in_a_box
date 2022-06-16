#!/usr/bin/env python3

import subprocess as sp
import tkinter as tk 
from signal import pause
from pynput.keyboard import Listener
import asyncio

COMMAND = "mplayer -fs ./data/SampleVideo_1280x720_1mb_italian.mp4 &"

key = 'q'    

def on_press(key):
    if getattr(key, "char", None) == 'q':
        print("press Q")
        #sp.run(COMMAND.split(' '))
        asyncio.run(run(COMMAND))
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