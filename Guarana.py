from Roslina import Roslina
class Guarana(Roslina):

    def __init__(self, a, b, s):
        self.nazwa = "Guarana"
        self.sila = 0
        self.inicjatywa = 0
        self.x = a
        self.y = b
        self.swiat = s
        self.wiek = 0

    def rysowanie(self):
        return "#d03232"

    def rozmnozSie(self, a, b):
        return Guarana(a, b, self.swiat)

    def kolizja(self, other):
        other.setSila(other.getSila() + 3)
        self.swiat.events.append("Sila [" + other.getNazwa() + "] wynosi teraz " + str(other.getSila()))
