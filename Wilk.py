from Organizm import Organizm
from Swiat import Swiat
from Zwierze import Zwierze
from tkinter import *


class Wilk(Zwierze):
    def __init__(self, a, b, s):
        self.nazwa = "Wilk"
        self.sila = 9
        self.inicjatywa = 5
        self.x = a
        self.y = b
        self.swiat = s
        self.wiek = 0

    def rysowanie(self):
        return "#8A8787"

    def rozmnozSie(self, a, b):
        return Wilk(a, b, self.swiat)
