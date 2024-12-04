import random

from Zwierze import Zwierze
from main import czyOdpiera
from main import czyZwierze

class Zolw(Zwierze):
    def __init__(self, a, b, s):
        self.nazwa = "Zolw"
        self.sila = 2
        self.inicjatywa = 1
        self.x = a
        self.y = b
        self.swiat = s
        self.wiek = 0

    def rysowanie(self):
        return "#aac79b"

    def rozmnozSie(self, a, b):
        return Zolw(a, b, self.swiat)

    def akcja(self, c):
        n = random.randint(1, 4)
        if n == 1:
            while True:
                n = random.randint(1, 4)
                if n == 1:
                    if self.x < self.swiat.getN() - 1:
                        if self.swiat.czyPuste(self.x + 1, self.y):
                            self.swiat.usunOrganizm(self)
                            self.x += 1
                            self.swiat.dodajOrganizm(self)
                            break
                        else:
                            self.kolizja(self.swiat.getOrganizmy()[self.x + 1][self.y])
                            break
                elif n == 2:
                    if self.x > 0:
                        if self.swiat.czyPuste(self.x - 1, self.y):
                            self.swiat.usunOrganizm(self)
                            self.x -= 1
                            self.swiat.dodajOrganizm(self)
                            break
                        else:
                            self.kolizja(self.swiat.getOrganizmy()[self.x - 1][self.y])
                            break
                elif n == 3:
                    if self.y < self.swiat.getM() - 1:
                        if self.swiat.czyPuste(self.x, self.y + 1):
                            self.swiat.usunOrganizm(self)
                            self.y += 1
                            self.swiat.dodajOrganizm(self)
                            break
                        else:
                            self.kolizja(self.swiat.getOrganizmy()[self.x][self.y + 1])
                            break
                elif n == 4:
                    if self.y > 0:
                        if self.swiat.czyPuste(self.x, self.y - 1):
                            self.swiat.usunOrganizm(self)
                            self.y -= 1
                            self.swiat.dodajOrganizm(self)
                            break
                        else:
                            self.kolizja(self.swiat.getOrganizmy()[self.x][self.y - 1])
                            break

    def kolizja(self, other):
        if self.nazwa == other.getNazwa():
            if (
                self.swiat.czyPuste(self.x + 1, self.y)
                or self.swiat.czyPuste(self.x - 1, self.y)
                or self.swiat.czyPuste(self.x, self.y + 1)
                or self.swiat.czyPuste(self.x, self.y - 1)
                or self.swiat.czyPuste(other.getX() + 1, other.getY())
                or self.swiat.czyPuste(other.getX() - 1, other.getY())
                or self.swiat.czyPuste(other.getX(), other.getY()+ 1)
            ):
                while True:
                    n = random.randint(1, 4)

                    # Sprawdzanie pol wokół this
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

                    # Sprawdzanie pol wokół other
                    if n == 1:
                        if self.x < self.swiat.getN() - 1:
                            if self.swiat.czyPuste(other.getX() + 1, other.getY()):
                                self.swiat.dodajOrganizm(self.rozmnozSie(self.x + 1, self.y))
                                break
                    elif n == 2:
                        if self.x > 0:
                            if self.swiat.czyPuste(other.getX() - 1, other.getY()):
                                self.swiat.dodajOrganizm(self.rozmnozSie(self.x - 1, self.y))
                                break
                    elif n == 3:
                        if self.y < self.swiat.getM() - 1:
                            if self.swiat.czyPuste(other.getX(), other.getY() + 1):
                                self.swiat.dodajOrganizm(self.rozmnozSie(self.x, self.y + 1))
                                break
                    elif n == 4:
                        if self.y > 0:
                            if self.swiat.czyPuste(other.getX(), other.getY() - 1):
                                self.swiat.dodajOrganizm(self.rozmnozSie(self.x, self.y - 1))
                                break
        else:
            if self.sila >= other.getSila():
                if czyZwierze(other.getNazwa()):
                    pass
                    # cout << "[" << nazwa << "] zabija [" << other.getNazwa() << "]        " << endl
                else:
                    self.swiat.events.append(
                        "[" + self.nazwa + "] zjada [" + other.getNazwa() + "] na polu (" + str(self.x) + ", " + str(self.y) + ")"
                    )
                    other.kolizja(self)
                if other.getNazwa() == "Czlowiek":
                    self.swiat.is_alive = False
                self.swiat.usunOrganizm(other)
                self.swiat.usunOrganizm(self)
                self.setX(other.getX())
                self.setY(other.getY())
                self.swiat.dodajOrganizm(self)
            else:
                if other.getSila() >= 5:
                    self.swiat.events.append(
                        "[" + other.getNazwa() + "] zabija [" + self.nazwa + "] na polu (" + str(self.x) + ", " + str(self.y) + ")"
                    )
                    self.swiat.usunOrganizm(self)
                else:
                    self.swiat.events.append(
                        "[Zolw] odpiera atak [" + other.getNazwa() + "] na polu (" + str(self.x) + ", " + str(self.y) + ")"
                    )
