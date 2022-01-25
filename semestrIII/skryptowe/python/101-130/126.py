class Kolo:
    def __init__(self, r):
        self.r = r

    def pole(self):
        return 3.14 * self.r * self.r

    def obwod(self):
        return 2 * 3.14 * self.r

    def dlugosc_okregu(self):
        return self.pole() / self.obwod()
