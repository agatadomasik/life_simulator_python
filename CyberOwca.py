import random

from Organizm import Organizm
from Swiat import Swiat
from Zwierze import Zwierze
from tkinter import *

from main import czyOdpiera, czyUcieka, czyZwierze


class CyberOwca(Zwierze):
    def __init__(self, a, b, s):
        self.nazwa = "CyberOwca"
        self.sila = 11
        self.inicjatywa = 4
        self.x = a
        self.y = b
        self.swiat = s
        self.wiek = 0

    def rysowanie(self):
        return "#fc00e3"

    def rozmnozSie(self, a, b):
        return CyberOwca(a, b, self.swiat)

    def akcja(self, c):
        if self.swiat.czyBarszcz():
            x = self.swiat.gdzieBarszcz(self).getX()
            y = self.swiat.gdzieBarszcz(self).getY()

            if self.x < x:
                if self.swiat.czyPuste(self.x + 1, self.y):
                    self.swiat.usunOrganizm(self)
                    self.x += 1
                    self.swiat.dodajOrganizm(self)
                else:
                    self.kolizja(self.swiat.getOrganizmy()[self.x + 1][self.y])
            elif self.x > x:
                if self.swiat.czyPuste(self.x - 1, self.y):
                    self.swiat.usunOrganizm(self)
                    self.x -= 1
                    self.swiat.dodajOrganizm(self)
                else:
                    self.kolizja(self.swiat.getOrganizmy()[self.x - 1][self.y])
            elif self.y < y:
                if self.swiat.czyPuste(self.x, self.y + 1):
                    self.swiat.usunOrganizm(self)
                    self.y += 1
                    self.swiat.dodajOrganizm(self)
                else:
                    self.kolizja(self.swiat.getOrganizmy()[self.x][self.y + 1])
            elif self.y > y:
                if self.swiat.czyPuste(self.x, self.y - 1):
                    self.swiat.usunOrganizm(self)
                    self.y -= 1
                    self.swiat.dodajOrganizm(self)
                else:
                    self.kolizja(self.swiat.getOrganizmy()[self.x][self.y - 1])

        else:
            super().akcja(c)

