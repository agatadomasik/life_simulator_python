import random

from Zwierze import Zwierze
from main import czyOdpiera
from main import czyZwierze


class Antylopa(Zwierze):
    def __init__(self, a, b, s):
        self.nazwa = "Antylopa"
        self.sila = 4
        self.inicjatywa = 4
        self.x = a
        self.y = b
        self.swiat = s
        self.wiek = 0

    def rysowanie(self):
        return "#ffc990"

    def rozmnozSie(self, a, b):
        return Antylopa(a, b, self.swiat)

    def akcja(self, c):
        while True:
            n = random.randint(1, 4)
            if n == 1:
                if self.x < self.swiat.getN() - 2:
                    if self.swiat.czyPuste(self.x + 2, self.y):
                        self.swiat.usunOrganizm(self)
                        self.x += 2
                        self.swiat.dodajOrganizm(self)
                        break
                    else:
                        self.kolizja(self.swiat.getOrganizmy()[self.x + 2][self.y])
                        break
            elif n == 2:
                if self.x > 1:
                    if self.swiat.czyPuste(self.x - 2, self.y):
                        self.swiat.usunOrganizm(self)
                        self.x -= 2
                        self.swiat.dodajOrganizm(self)
                        break
                    else:
                        self.kolizja(self.swiat.getOrganizmy()[self.x - 2][self.y])
                        break
            elif n == 3:
                if self.y < self.swiat.getM() - 2:
                    if self.swiat.czyPuste(self.x, self.y + 2):
                        self.swiat.usunOrganizm(self)
                        self.y += 2
                        self.swiat.dodajOrganizm(self)
                        break
                    else:
                        self.kolizja(self.swiat.getOrganizmy()[self.x][self.y + 2])
                        break
            elif n == 4:
                if self.y > 1:
                    if self.swiat.czyPuste(self.x, self.y - 2):
                        self.swiat.usunOrganizm(self)
                        self.y -= 2
                        self.swiat.dodajOrganizm(self)
                        break
                    else:
                        self.kolizja(self.swiat.getOrganizmy()[self.x][self.y - 2])
                        break

    def kolizja(self, other):
        if self.nazwa == other.getNazwa():
            if (self.swiat.czyPuste(self.x + 2, self.y) or self.swiat.czyPuste(self.x - 2, self.y) or
                    self.swiat.czyPuste(self.x, self.y + 2) or self.swiat.czyPuste(self.x, self.y - 2) or
                    self.swiat.czyPuste(other.getX() + 2, other.getY()) or self.swiat.czyPuste(other.getX() - 2,
                                                                                               other.getY()) or
                    self.swiat.czyPuste(other.getX(), other.getY() + 2) or self.swiat.czyPuste(other.getX(),
                                                                                               other.getY() - 2)):

                while True:
                    n = random.randint(1, 4)

                    # Sprawdzanie pól wokół self
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

                    # Sprawdzanie pól wokół other
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
                if not czyOdpiera(other):
                    if czyZwierze(other.getNazwa()):
                        # cout << endl << "[" << nazwa << "] zabija [" << other->getNazwa() << "]" << endl;
                        pass
                    else:
                        other.kolizja(self)
                    if other.getNazwa() == "Czlowiek":
                        self.swiat.is_alive = False
                    self.swiat.usunOrganizm(other)
                    self.swiat.usunOrganizm(self)
                    self.setX(other.getX())
                    self.setY(other.getY())
                    self.swiat.dodajOrganizm(self)
                else:
                    other.kolizja(self)
            else:
                if czyZwierze(other.getNazwa()):
                    n = random.randint(1, 4)
                    if n == 1:
                        self.swiat.events.append(
                            "[" + other.getNazwa() + "] zabija [" + self.nazwa + "] na polu (" + str(
                                self.x) + ", " + str(self.y) + ")")
                        self.swiat.usunOrganizm(self)
                    else:
                        if self.swiat.getOrganizmy()[self.x][self.y] == self:
                            self.akcja('a')
                            self.swiat.events.append(
                                "[" + self.nazwa + "] ucieka przed [" + other.getNazwa() + "] na pole (" + str(
                                    self.x) + ", " + str(self.y) + ")")
                else:
                    other.kolizja(self)

