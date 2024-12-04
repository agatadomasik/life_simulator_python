from Roslina import Roslina
class WilczeJagody(Roslina):
    def __init__(self, a, b, s):
        self.nazwa = "WilczeJagody"
        self.sila = 99
        self.inicjatywa = 0
        self.x = a
        self.y = b
        self.swiat = s
        self.wiek = 0

    def rysowanie(self):
        return "#5737b7"

    def rozmnozSie(self, a, b):
        return WilczeJagody(a, b, self.swiat)