class AN47 (object):
    def __init__(self, clips_left):
        self.aim = True
        self.in_clips = 30
        self.clips_left = clips_left

    def reload(self):
        if self.clips_left > 0:
            self.in_clips = 30
            self.clips_left -= 1

    def