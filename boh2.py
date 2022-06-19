#!/usr/bin/env python3

import time
import mpv
player = mpv.MPV(ytdl=True)
player.play('./data/video_english.mp4')
player.wait_for_playback()
time.sleep(2)
player.pause()

