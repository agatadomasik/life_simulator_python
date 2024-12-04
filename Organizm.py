from abc import ABC, abstractmethod

class Organizm(ABC):
    def __init__(self):
        self.nazwa = None
        self.sila = 0
        self.inicjatywa = 0
        self.x = 0
        self.y = 0
        self.wiek = 0
        self.swiat = None

    @abstractmethod
    def akcja(self, c):
        pass

    @abstractmethod
    def kolizja(self, other):
        pass

    @abstractmethod
    def rozmnozSie(self, x, y):
        pass

    @abstractmethod
    def rysowanie(self):
        pass

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getNazwa(self):
        return self.nazwa

    def getSila(self):
        return self.sila if self else 0

    def getInicjatywa(self):
        return self.inicjatywa

    def getWiek(self):
        return self.wiek

    def setX(self, a):
        self.x = a

    def setY(self, b):
        self.y = b

    def setSila(self, a):
        self.sila = a

    def zwiekszWiek(self):
        self.wiek += 1

    def setWiek(self, a):
        self.wiek = a

    def clean(self):
        self.swiat = None

    def getTura(self):
        return 0

    def getPower(self):
        return False