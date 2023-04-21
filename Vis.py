class Vis:

    MAX_TIGHTNESS = 5

    def __init__(self):
        self.tightness = 0

    def visser(self):
        if self.tightness < self.MAX_TIGHTNESS:
            self.tightness += 1

    def devisser(self):
        if self.tightness > 0:
            self.tightness -= 1

    def __str__(self):
        return "Vis avec serrage de {}".format(self.tightness)

