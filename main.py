# Organizm import Organizm
from Window import Window


def czyZwierze(s):
    if s in ["Wilk", "Owca", "Lis", "Zolw", "Antylopa", "Czlowiek"]:
        return True
    return False

def czyOdpiera(o):
    if o.getNazwa() == "Zolw":
        return True
    return False

def czyUcieka(o):
    if o.getNazwa() == "Antylopa":
        return True
    return False
def main():
    board = Window()

if __name__ == "__main__":
    from Swiat import Swiat
    main()