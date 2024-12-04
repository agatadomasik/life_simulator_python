from Roslina import Roslina


class Trawa(Roslina):
    def __init__(self, a, b, s):
        self.nazwa = "Trawa"
        self.sila = 0
        self.inicjatywa = 0
        self.x = a
        self.y = b
        self.swiat = s
        self.wiek = 0

    def rysowanie(self):
        return "#259d00"

    def rozmnozSie(self, a, b):
        return Trawa(a, b, self.swiat)