from Roslina import Roslina
import random

from main import czyZwierze


class BarszczSosnowskiego(Roslina):
    def __init__(self, a, b, s):
        self.nazwa = "BarszczSosnowskiego"
        self.sila = 10
        self.inicjatywa = 0
        self.x = a
        self.y = b
        self.swiat = s
        self.wiek = 0

    def rysowanie(self):
        return "#8f2065"

    def rozmnozSie(self, a, b):
        return BarszczSosnowskiego(a, b, self.swiat)

    def akcja(self, c):
        if (
            self.swiat.czyPuste(self.x + 1, self.y)
            or self.swiat.czyPuste(self.x - 1, self.y)
            or self.swiat.czyPuste(self.x, self.y + 1)
            or self.swiat.czyPuste(self.x, self.y - 1)
        ):
            while True:
                n =  random.randrange(1, 5)

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

        if self.x < self.swiat.getN() - 1:
            if not self.swiat.czyPuste(self.x + 1, self.y):
                self.kolizja(self.swiat.getOrganizmy()[self.x + 1][self.y])

        if self.x > 0:
            if not self.swiat.czyPuste(self.x - 1, self.y):
                self.kolizja(self.swiat.getOrganizmy()[self.x - 1][self.y])

        if self.y < self.swiat.getM() - 1:
            if not self.swiat.czyPuste(self.x, self.y + 1):
                self.kolizja(self.swiat.getOrganizmy()[self.x][self.y + 1])

        if self.y > 0:
            if not self.swiat.czyPuste(self.x, self.y - 1):
                self.kolizja(self.swiat.getOrganizmy()[self.x][self.y - 1])

    def kolizja(self, other):
        from CyberOwca import CyberOwca
        if czyZwierze(other.getNazwa()):
            self.swiat.usunOrganizm(other)
            if other.getNazwa() == "Czlowiek":
                self.swiat.is_alive = False
            self.swiat.events.append("[BarszczSosnowskiego] zabija [" + other.getNazwa() + "] na polu (" +
                                     str(other.getX()) + " " + str(other.getY) + ")")
        elif isinstance(other, CyberOwca):
            self.swiat.events.append("[CyberOwca] zjada [BarszczSosnowskiego] na polu (" +
                                     str(self.x) + ", " + str(self.y) + ")")
            pass