from Organizm import Organizm
from Swiat import Swiat
from Zwierze import Zwierze
from tkinter import *
class Owca(Zwierze):
    def __init__(self, a, b, s):
        self.nazwa = "Owca"
        self.sila = 4
        self.inicjatywa = 4
        self.x = a
        self.y = b
        self.swiat = s
        self.wiek = 0

    def rysowanie(self):
        return "#ded8c9"

    def rozmnozSie(self, a, b):
        return Owca(a, b, self.swiat)