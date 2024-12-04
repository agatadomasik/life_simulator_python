import random
from Zwierze import Zwierze


class Lis(Zwierze):
    def __init__(self, a, b, s):
        self.nazwa = "Lis"
        self.sila = 3
        self.inicjatywa = 7
        self.x = a
        self.y = b
        self.swiat = s
        self.wiek = 0

    def rysowanie(self):
        return "#ff8d3c"

    def rozmnozSie(self, a, b):
        return Lis(a, b, self.swiat)

    def akcja(self, c):
        if ((self.x < self.swiat.getN() - 1 and ((self.swiat.getOrganizmy()[self.x + 1][self.y] is not None and self.swiat.getOrganizmy()[self.x + 1][self.y].getSila() <= self.sila) or (self.swiat.getOrganizmy()[self.x + 1][self.y] is None))) or
                (self.x > 0 and ((self.swiat.getOrganizmy()[self.x - 1][self.y] is not None and self.swiat.getOrganizmy()[self.x - 1][self.y].getSila() <= self.sila) or (self.swiat.getOrganizmy()[self.x - 1][self.y] is None))) or
                (self.y < self.swiat.getM() - 1 and ((self.swiat.getOrganizmy()[self.x][self.y + 1] is not None and self.swiat.getOrganizmy()[self.x][self.y + 1].getSila() <= self.sila) or (self.swiat.getOrganizmy()[self.x][self.y + 1] is None))) or
                (self.y > 0 and (self.swiat.getOrganizmy()[self.x][self.y - 1] is not None and self.swiat.getOrganizmy()[self.x][self.y - 1].getSila() <= self.sila) or (self.swiat.getOrganizmy()[self.x][self.y - 1] is None))):
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
                            if self.swiat.getOrganizmy()[self.x + 1][self.y].getSila() <= self.sila:
                                self.kolizja(self.swiat.getOrganizmy()[self.x + 1][self.y])
                                break
                            else:
                                self.swiat.events.append("[Lis] wyczuwa silniejszy organizm")
                elif n == 2:
                    if self.x > 0:
                        if self.swiat.czyPuste(self.x - 1, self.y):
                            self.swiat.usunOrganizm(self)
                            self.x -= 1
                            self.swiat.dodajOrganizm(self)
                            break
                        else:
                            if self.swiat.getOrganizmy()[self.x - 1][self.y].getSila() <= self.sila:
                                self.kolizja(self.swiat.getOrganizmy()[self.x - 1][self.y])
                                break
                            else:
                                self.swiat.events.append("[Lis] wyczuwa silniejszy organizm")
                elif n == 3:
                    if self.y < self.swiat.getM() - 1:
                        if self.swiat.czyPuste(self.x, self.y + 1):
                            self.swiat.usunOrganizm(self)
                            self.y += 1
                            self.swiat.dodajOrganizm(self)
                            break
                        else:
                            if self.swiat.getOrganizmy()[self.x][self.y + 1].getSila() <= self.sila:
                                self.kolizja(self.swiat.getOrganizmy()[self.x][self.y + 1])
                                break
                            else:
                                self.swiat.events.append("[Lis] wyczuwa silniejszy organizm")
                elif n == 4:
                    if self.y > 0:
                        if self.swiat.czyPuste(self.x, self.y - 1):
                            self.swiat.usunOrganizm(self)
                            self.y -= 1
                            self.swiat.dodajOrganizm(self)
                            break
                        else:
                            if self.swiat.getOrganizmy()[self.x][self.y - 1].getSila() <= self.sila:
                                self.kolizja(self.swiat.getOrganizmy()[self.x][self.y - 1])
                                break
                            else:
                                self.swiat.events.append("[Lis] wyczuwa silniejszy organizm")
        else:
            self.swiat.events.append("[Lis] nie ma gdzie sie poruszyc")


