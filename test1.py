#!/usr/bin/env python3

import subprocess as sp
from gpiozero import Button
from signal import pause

button = Button(2)


def runvideo():
    sp.check_output(["mplayer", "-fs", "-ao", " alsa",
                     "/home/neum/Scaricati/SampleVideo_1280x720_10mb.mp4"])


button.when_pressed = runvideo
pause()
