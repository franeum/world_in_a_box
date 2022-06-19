import pathlib
from mpv import MPV

class Video():
    def __init__(self):
        self.video = MPV()

    def set_path(self, path):
        self.path = str(path)

    def play(self):
        self.video.pause = False
        self.video.play(self.path)

    def toggle_pause(self):
        self.video.pause = not self.video.pause