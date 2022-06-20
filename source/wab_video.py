from mpv import MPV


class Video():
    def __init__(self):
        self.video = MPV()

    def set_path(self, path):
        self.path = str(path)

    def set_callback(self, callback, *args):
        p = self.video

        @p.event_callback('END_FILE')
        def finefile(event):
            if event['event_id'] == 7:
                print(args)
                callback(args)

    def play(self):
        self.video.pause = False
        self.video.fullscreen = True
        self.video.play(self.path)

    def toggle_pause(self):
        self.video.pause = not self.video.pause
