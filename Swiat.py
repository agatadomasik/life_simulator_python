import random
from Organizm import Organizm

class Swiat:
    def __init__(self, a, b):
        self.N = a
        self.M = b
        self.is_alive = True
        self.organizmy = [[None for _ in range(self.M)] for _ in range(self.N)]
        self.events = []

    @staticmethod
    def getListaOrganizmow():
        return ["Antylopa", "Lis", "Owca", "Wilk", "Zolw", "BarszczSosnowskiego", "Guarana", "Mlecz", "Trawa", "WilczeJagody"]

    def rysujSwiat(self, x, y):
        # gorna ramka
        print(chr(201) + chr(205) * (self.N * 2 + 1) + chr(187))

        # dolna ramka
        print(chr(200) + chr(205) * (self.N * 2 + 1) + chr(188))

        # boki
        for i in range(self.M):
            print(chr(186) + " " + chr(186))

        # organizmy
        print(f"{x} {y}")
        for i in range(self.M):
            for j in range(self.N):
                if self.organizmy[j][i] is None:
                    print("  ", end="")
                else:
                    self.organizmy[j][i].rysowanie()
                    print(" ", end="")
            print()

    def dodajOrganizm(self, o):
        x = o.getX()
        y = o.getY()
        if x < self.N and y < self.M:
            self.organizmy[x][y] = o

    def usunOrganizm(self, o):
        x = o.getX()
        y = o.getY()
        self.organizmy[x][y] = None

    def getN(self):
        return self.N

    def getM(self):
        return self.M

    def getOrganizmy(self):
        return self.organizmy

    def czyPuste(self, x, y):
        if x < self.N and y < self.M and x >= 0 and y >= 0:
            if self.organizmy[x][y] is None:
                return True
        return False

    def wyczysc(self):
        for i in range(self.N):
            for j in range(self.M):
                self.organizmy[i][j] = None

    def getTura(self):
        for i in range(self.N):
            for j in range(self.M):
                if self.organizmy[i][j] is not None and self.organizmy[i][j].getNazwa() == "Czlowiek":
                    return self.organizmy[i][j].getTura()
        return 0

    def setN(self, a):
        self.N = a

    def setM(self, a):
        self.M = a

    def wykonajTure(self, tmp, z):
        i = 0
        while i < len(tmp):
            if tmp[i].getNazwa() != "Czlowiek":
                if self.organizmy[tmp[i].getX()][tmp[i].getY()] == tmp[i]:
                    tmp[i].akcja(z)
                    i += 1
                else:
                    tmp.pop(i)
            else:
                tmp[i].akcja(z)
                i += 1

    def getVector(self):
        # dodawanie do listy
        w = []
        for i in range(self.N):
            for j in range(self.M):
                if self.organizmy[i][j] is not None:
                    w.append(self.organizmy[i][j])
                    self.organizmy[i][j].zwiekszWiek()

        # sortowanie listy
        for i in range(len(w)):
            for j in range(1, len(w) - i):
                if w[j - 1].getInicjatywa() < w[j].getInicjatywa():
                    temp = w[j - 1]
                    w[j - 1] = w[j]
                    w[j] = temp
                elif w[j - 1].getInicjatywa() == w[j].getInicjatywa() and w[j - 1].getWiek() < w[j].getWiek():
                    temp = w[j - 1]
                    w[j - 1] = w[j]
                    w[j] = temp
        return w
    def generuj(self):
         from Czlowiek import Czlowiek
         from Wilk import Wilk
         from Owca import Owca
         from Lis import Lis
         from Zolw import Zolw
         from Antylopa import Antylopa
         from Trawa import Trawa
         from Mlecz import Mlecz
         from WilczeJagody import WilczeJagody
         from BarszczSosnowskiego import BarszczSosnowskiego
         from Guarana import Guarana
         from CyberOwca import CyberOwca

         for _ in range(3):
             tmp = [[0] * 2 for _ in range(11)]

             for j in range(11):
                 tmp[j][0] = random.randint(0, self.N - 1)
                 tmp[j][1] = random.randint(0, self.M - 1)

             tab = [None] * 11
             tab[0] = Wilk(tmp[0][0], tmp[0][1], self)
             tab[1] = Owca(tmp[1][0], tmp[1][1], self)
             tab[2] = Lis(tmp[2][0], tmp[2][1], self)
             tab[3] = Zolw(tmp[3][0], tmp[3][1], self)
             tab[4] = Antylopa(tmp[4][0], tmp[4][1], self)
             tab[5] = Trawa(tmp[5][0], tmp[5][1], self)
             tab[6] = Mlecz(tmp[6][0], tmp[6][1], self)
             tab[7] = Guarana(tmp[7][0], tmp[7][1], self)
             tab[8] = WilczeJagody(tmp[8][0], tmp[8][1], self)
             tab[9] = BarszczSosnowskiego(tmp[9][0], tmp[9][1], self)
             tab[10] = CyberOwca(tmp[10][0], tmp[10][1], self)

             #for j in range(11):
                 #self.dodajOrganizm(tab[j])

         self.dodajOrganizm(BarszczSosnowskiego(10,10,self))
         self.dodajOrganizm(BarszczSosnowskiego(7,15,self))
         self.dodajOrganizm(CyberOwca(5,6,self))

         c1 = Czlowiek(0, 0, self)
         self.dodajOrganizm(c1)

    def getPower(self):
        for i in range(self.N):
            for j in range(self.M):
                if self.organizmy[i][j] is not None and self.organizmy[i][j].getNazwa() == "Czlowiek":
                    return self.organizmy[i][j].getPower()
        return False

    def czyBarszcz(self):
        for i in range(self.N):
            for j in range(self.M):
                if self.organizmy[i][j] is not None:
                    if self.organizmy[i][j].getNazwa() == 'BarszczSosnowskiego':
                        return True
        return False

    def gdzieBarszcz(self, organizm: Organizm):
        rows = len(self.organizmy)
        if rows == 0:
            return None

        cols = len(self.organizmy[0])
        if cols == 0:
            return None

        najblizsza_x = None
        najblizsza_y = None
        najmniejsza_odleglosc = float('inf')

        for i in range(rows):
            for j in range(cols):
                if self.organizmy[i][j] != None and self.organizmy[i][j].getNazwa() == 'BarszczSosnowskiego':
                    odleglosc = abs(i - organizm.getX()) + abs(j - organizm.getY())
                    if odleglosc < najmniejsza_odleglosc:
                        najmniejsza_odleglosc = odleglosc
                        najblizsza_x = i
                        najblizsza_y = j

        return self.organizmy[najblizsza_x][najblizsza_y]