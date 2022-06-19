#!/usr/bin/env python3

import asyncio
import subprocess as sp
from gpiozero import Button
from signal import pause

button = Button(23)
counter = 0

def runvideo(push):
       global counter
       if (push.is_active):
              print(f"ciao {push}: {counter}")
              counter += 1
              asyncio.run(run(
                     "mplayer -fs -ao alsa ./data/video_italian.mp4 &"))

async def run(cmd):
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)

    await proc.communicate()

    print(f'[{cmd!r} exited with {proc.returncode}]')

button.when_pressed = runvideo
pause()
