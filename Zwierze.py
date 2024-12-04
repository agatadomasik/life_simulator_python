import random
from Organizm import Organizm
from main import czyZwierze
from main import czyOdpiera
from main import czyUcieka


class Zwierze(Organizm):
    def rozmnozSie(self, x, y):
        return None

    def rysowanie(self):
        return None

    def akcja(self, c):
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
            if (self.swiat.czyPuste(self.x + 1, self.y) or self.swiat.czyPuste(self.x - 1, self.y) or
                    self.swiat.czyPuste(self.x, self.y + 1) or self.swiat.czyPuste(self.x, self.y - 1) or
                    self.swiat.czyPuste(other.getX() + 1, other.getY()) or self.swiat.czyPuste(other.getX() - 1,
                                                                                               other.getY()) or
                    self.swiat.czyPuste(other.getX(), other.getY() + 1) or self.swiat.czyPuste(other.getX(),
                                                                                               other.getY() - 1)):
                while True:
                    rand_num = random.randint(1, 4)

                    if rand_num == 1:
                        if self.x < self.swiat.getN() - 1:
                            if self.swiat.czyPuste(self.x + 1, self.y):
                                self.swiat.dodajOrganizm(self.rozmnozSie(self.x + 1, self.y))
                                self.swiat.events.append("Narodziny [" + self.getNazwa() + "]")
                            break
                    elif rand_num == 2:
                        if self.x > 0:
                            if self.swiat.czyPuste(self.x - 1, self.y):
                                self.swiat.dodajOrganizm(self.rozmnozSie(self.x - 1, self.y))
                                self.swiat.events.append("Narodziny [" + self.getNazwa() + "]")
                    elif rand_num == 3:
                        if self.y < self.swiat.getM() - 1:
                            if self.swiat.czyPuste(self.x, self.y + 1):
                                self.swiat.dodajOrganizm(self.rozmnozSie(self.x, self.y + 1))
                                self.swiat.events.append("Narodziny [" + self.getNazwa() + "]")
                                break
                    elif rand_num == 4:
                        if self.y > 0:
                            if self.swiat.czyPuste(self.x, self.y - 1):
                                self.swiat.dodajOrganizm(self.rozmnozSie(self.x, self.y - 1))
                                self.swiat.events.append("Narodziny [" + self.getNazwa() + "]")
                                break
                    if rand_num == 1:
                        if self.x < self.swiat.getN() - 1:
                            if self.swiat.czyPuste(other.getX() + 1, other.getY()):
                                self.swiat.dodajOrganizm(self.rozmnozSie(self.x + 1, self.y))
                                self.swiat.events.append("Narodziny [" + self.getNazwa() + "]")
                                break
                            elif rand_num == 2:
                                if self.x > 0:
                                    if self.swiat.czyPuste(other.getX() - 1, other.getY()):
                                        self.swiat.dodajOrganizm(self.rozmnozSie(self.x - 1, self.y))
                                        self.swiat.events.append("Narodziny [" + self.getNazwa() + "]")
                                        break
                            elif rand_num == 3:
                                if self.x > 0:
                                    if self.swiat.czyPuste(other.getX(), other.getY() + 1):
                                        self.swiat.dodajOrganizm(self.rozmnozSie(self.x, self.y + 1))
                                        self.swiat.events.append("Narodziny [" + self.getNazwa() + "]")
                                        break
                            elif rand_num == 4:
                                if self.x > 0:
                                    if self.swiat.czyPuste(other.getX(), other.getY() - 1):
                                        self.swiat.dodajOrganizm(self.rozmnozSie(self.x, self.y - 1))
                                        self.swiat.events.append("Narodziny [" + self.getNazwa() + "]")
                                        break
        else:
            if self.sila >= other.getSila():
                if not czyOdpiera(other):
                    if not czyUcieka(other):
                        if other.getNazwa() == "Czlowiek":
                            self.swiat.is_alive = False
                        if czyZwierze(other.getNazwa()):
                            self.swiat.events.append(
                                "[" + self.nazwa + "] zabija [" + other.getNazwa() + "] na polu (" + str(
                                    other.getX()) + ", " + str(other.getY()) + ")")
                        else:
                            self.swiat.events.append(
                                "[" + self.nazwa + "] zjada [" + other.getNazwa() + "] na polu (" + str(
                                    other.getX()) + ", " + str(other.getY()) + ")")
                            other.kolizja(self)
                        self.swiat.usunOrganizm(other)
                        self.swiat.usunOrganizm(self)
                        self.setX(other.getX())
                        self.setY(other.getY())
                        self.swiat.dodajOrganizm(self)
                    else:
                        self.swiat.usunOrganizm(self)
                        self.setX(other.getX())
                        self.setY(other.getY())
                        other.kolizja(self)
                        self.swiat.dodajOrganizm(self)
                else:
                    other.kolizja(self)
            else:
                self.swiat.events.append(
                    "[" + other.getNazwa() + "] zabija [" + self.nazwa + "] na polu (" + str(
                        other.getX()) + ", " + str(other.getY()) + ")")
                if self.nazwa == "Czlowiek":
                    self.swiat.is_alive = False
                self.swiat.usunOrganizm(self)
