def leltar(szoveg1, szoveg2 = ""):
    if not isinstance(szoveg1, str):
        return {}
    elif not isinstance(szoveg2, str):
        szoveg2 = ""

    szavak = szoveg1.split(',')
    szotar = {}

    for szo in szavak:
        szo = szo.strip()

        if szo and szo != szoveg2:
            szotar[szo] = szotar.get(szo, 0) + 1

    szotar = {szo: db for szo, db in szotar.items() if db != 13}

    return szotar

print(leltar("alma, körte, alma, szilva, körte, körte", "alma"))
print(leltar("alma, alma, alma, alma, alma, alma, alma, alma, alma, alma, alma, alma, alma", "körte"))

class Kalandor:

    TARGY_ARAK = {
        "kard": 40,
        "pajzs": 30,
        "íj": 40,
        "Bájital": 20,
        "Sisak": 50,
        "Vért": 60
    }

    def __init__(self, nev = "John Doe", eletero = 20, targyak = None):
        self.nev = nev if isinstance(nev,str) else "John Doe"
        self._eletero = eletero if isinstance(eletero,int) and eletero >= 0 else 20
        self.targyak = targyak if isinstance(targyak,list) else []
        self.arany = 100
        self.csapat = []

    @property
    def eletero(self):
        return self._eletero
    
    @eletero.setter
    def eletero(self, ertek):
        if isinstance(ertek, int) and ertek >= 0:
            self._eletero = ertek
        else:
            self._eletero = 0

    def __str__(self):
        targyak_str = ", ".join(self.targyak)
        csapat_str = ", ".join([k.nev for k in self.csapat])
        return f"{self.nev}|{self._eletero}|{self.arany}|{targyak_str}|{csapat_str}"

    def __iadd__(self, masik):
        if isinstance(masik, Kalandor) and masik not in self.csapat and masik != self:
            self.csapat.append(masik)
        if self not in masik.csapat and self != masik:
            masik.csapat.append(self)
        return self
    
    def harc(self, masik):
        if not isinstance(masik, Kalandor) or self._eletero == 0 or masik.eletero == 0:
            return  
        
        if len(self.targyak) > len(masik.targyak):
            self.eletero -= 2
            masik.eletero -= 5
        elif len(self.targyak) < len(masik.targyak):
            self.eletero -= 5
            masik.eletero -= 2
        else:
            self.eletero -= 3
            masik.eletero -= 3

    def vasarlas(self, targy):
        if not isinstance(targy, str) or targy not in self.TARGY_ARAK:
            return 

        ar = self.TARGY_ARAK[targy]
        if self.arany >= ar:
            self.arany -= ar
            self.targyak.append(targy)
        else:
            raise ArithmeticError("Nincs elég arany a vásárláshoz.")
        
# Példa kalandorok létrehozása
k1 = Kalandor("Arthur", 25, ["kard", "pajzs"])
k2 = Kalandor("Lancelot", 30)

# Kiíratás
print(k1)
print(k2)

# Kalandorok csapathoz adása
k1 += k2
print(k1)

# Harc
k1.harc(k2)
print(k1)
print(k2)

# Vásárlás
k1.vasarlas("gyuru")
print(k1)