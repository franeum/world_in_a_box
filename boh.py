#!/usr/bin/env python3

from mplayer import Player
Player.exec_path = "/usr/bin/mplayer"

p = Player()
p.args = ["-vo xv"]
p.loadfile("./data/video_english.mp4")

