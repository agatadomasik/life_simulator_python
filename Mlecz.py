import random
from Roslina import Roslina
class Mlecz(Roslina):
    def __init__(self, a, b, s):
        self.nazwa = "Mlecz"
        self.sila = 0
        self.inicjatywa = 0
        self.x = a
        self.y = b
        self.swiat = s
        self.wiek = 0

    def rysowanie(self):
        return "#ffdd3d"

    def rozmnozSie(self, a, b):
        return Mlecz(a, b, self.swiat)

    def akcja(self, c):
        for i in range(3):
            if (self.swiat.czyPuste(self.x + 1, self.y) or self.swiat.czyPuste(self.x - 1, self.y) or
                    self.swiat.czyPuste(self.x, self.y + 1) or self.swiat.czyPuste(self.x, self.y - 1)):
                while True:
                    n = random.randrange(1, 5)

                    # Sprawdzanie pol wokol this
                    if n == 1:
                        if self.x < self.swiat.getN() - 1:
                            if self.swiat.czyPuste(self.x + 1, self.y):
                                self.swiat.dodajOrganizm(self.rozmnozSie(self.x + 1, self.y))
                                break
                    elif n == 2:
                        if self.x > 0:
                            if self.swiat.czyPuste(self.x - 1, self.y):
                                self.swiat.dodajOrganizm(self.rozmnozSie(self.x - 1, self.y))
                                break
                    elif n == 3:
                        if self.y < self.swiat.getM() - 1:
                            if self.swiat.czyPuste(self.x, self.y + 1):
                                self.swiat.dodajOrganizm(self.rozmnozSie(self.x, self.y + 1))
                                break
                    elif n == 4:
                        if self.y > 0:
                            if self.swiat.czyPuste(self.x, self.y - 1):
                                self.swiat.dodajOrganizm(self.rozmnozSie(self.x, self.y - 1))
                                break
