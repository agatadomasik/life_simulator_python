from Organizm import Organizm
import random


class Roslina(Organizm):
    def rozmnozSie(self, x, y):
        return None

    def rysowanie(self):
        return None

    def akcja(self, c):
        if (
                self.swiat.czyPuste(self.x + 1, self.y)
                or self.swiat.czyPuste(self.x - 1, self.y)
                or self.swiat.czyPuste(self.x, self.y + 1)
                or self.swiat.czyPuste(self.x, self.y - 1)
        ):
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

    def kolizja(self, other):
        pass
