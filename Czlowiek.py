from Zwierze import Zwierze
import random


class Czlowiek(Zwierze):
    def __init__(self, a, b, s):
        self.nazwa = "Czlowiek"
        self.sila = 5
        self.inicjatywa = 4
        self.x = a
        self.y = b
        self.swiat = s
        self.wiek = 0
        self.tura = 0
        self.wait = 0
        self.power = False

    def rysowanie(self):
        return "#00BBFF"

    def rozmnozSie(self, a, b):
        return Czlowiek(a, b, self.swiat)

    def akcja(self, c):
        if not self.power:
            if c == 'Right':
                self.tura += 1
                if self.x < self.swiat.getN() - 1:
                    if self.swiat.czyPuste(self.x + 1, self.y):
                        self.swiat.usunOrganizm(self)
                        self.x += 1
                        self.swiat.dodajOrganizm(self)
                    else:
                        self.kolizja(self.swiat.getOrganizmy()[self.x + 1][self.y])
            elif c == 'Left':
                self.tura += 1
                if self.x > 0:
                    if self.swiat.czyPuste(self.x - 1, self.y):
                        self.swiat.usunOrganizm(self)
                        self.x -= 1
                        self.swiat.dodajOrganizm(self)
                    else:
                        self.kolizja(self.swiat.getOrganizmy()[self.x - 1][self.y])
            elif c == 'Down':
                self.tura += 1
                if self.y < self.swiat.getM() - 1:
                    if self.swiat.czyPuste(self.x, self.y + 1):
                        self.swiat.usunOrganizm(self)
                        self.y += 1
                        self.swiat.dodajOrganizm(self)
                    else:
                        self.kolizja(self.swiat.getOrganizmy()[self.x][self.y + 1])
            elif c == 'Up':
                if self.y > 0:
                    self.tura += 1
                    if self.swiat.czyPuste(self.x, self.y - 1):
                        self.swiat.usunOrganizm(self)
                        self.y -= 1
                        self.swiat.dodajOrganizm(self)
                    else:
                        self.kolizja(self.swiat.getOrganizmy()[self.x][self.y - 1])
        else:
            if c == 'Right':
                self.tura += 1
                if self.x < self.swiat.getN() - 2:
                    if self.swiat.czyPuste(self.x + 2, self.y):
                        self.swiat.usunOrganizm(self)
                        self.x += 2
                        self.swiat.dodajOrganizm(self)
                    else:
                        self.kolizja(self.swiat.getOrganizmy()[self.x + 2][self.y])
            elif c == 'Left':
                self.tura += 1
                if self.x > 1:
                    if self.swiat.czyPuste(self.x - 2, self.y):
                        self.swiat.usunOrganizm(self)
                        self.x -= 2
                        self.swiat.dodajOrganizm(self)
                    else:
                        self.kolizja(self.swiat.getOrganizmy()[self.x - 2][self.y])
            elif c == 'Down':
                self.tura += 1
                if self.y < self.swiat.getM() - 2:
                    if self.swiat.czyPuste(self.x, self.y + 2):
                        self.swiat.usunOrganizm(self)
                        self.y += 2
                        self.swiat.dodajOrganizm(self)
                    else:
                        self.kolizja(self.swiat.getOrganizmy()[self.x][self.y + 2])
            elif c == 'Up':
                self.tura += 1
                if self.y > 0:
                    if self.swiat.czyPuste(self.x, self.y - 2):
                        self.swiat.usunOrganizm(self)
                        self.y -= 2
                        self.swiat.dodajOrganizm(self)
                    else:
                        self.kolizja(self.swiat.getOrganizmy()[self.x][self.y - 2])

        if (self.tura == -6 or self.tura == -5) and c != -32:
            n = random.randint(1, 2)
            if n == 1:
                self.power = False
            else:
                self.power = True

        if self.tura == -5 and c != -32:
            self.swiat.events.append("Szybkosc antylopy dezaktywowana")
            self.power = False

        if c == 'space' and self.tura >= 0:
            self.swiat.events.append("Szybkosc antylopy aktywowana")
            self.power = True
            self.tura = -10

    def getTura(self):
        return self.tura

    def getPower(self):
        return self.power

    def setTura(self, a):
        self.tura = a

    def setPower(self, power):
        self.power = power