import time

class CooldownError(Exception):
    pass

class Cooldown:
    def __init__(self, length: int = 5):
        self.start = time.time()
        self.length = length

    def reinit(self):
        self.start = time.time()

    def expired(self) -> bool:
        return self.start + self.length < time.time()

    def getremain(self) -> float:
        return abs(time.time() - self.start - self.length)