# Nev: Kis Bence Róbert
# Neptun: IFQA67
# h: h264560
#import collections

def utolso_x_szo(szoveg, szam):
    if not isinstance(szoveg, str) or not isinstance(szam, int) or szam <= 0:
        return "-"

    if any(c in szoveg for c in ['!', '.', ',', '?']):
        return "-"

    szavak = szoveg.split()

    if szam > len(szavak):
        return "-"

    last_word = szavak[-szam:]
    retStr = " ".join(last_word).capitalize() + "."
    
    return retStr

#üvölteni fogok
#print(utolso_x_szo('én vagyok a legnagyobb rajongód', 3))
#print(utolso_x_szo('vigyázni kell magamra, nincs b terv!', 4))
#print(utolso_x_szo('na most figyeld öcsikesz, azarát metriosz-zintosz', 2))
#print(utolso_x_szo('faszomat verjem bele az egész gecis python',6))

def karakter_modusz(szoveg):
    tmp = dict()
    if szoveg and type(szoveg) is str and szoveg.find("uwu") == -1:
        tmpStr = szoveg.replace(' ', '').replace('\n','')
        if not tmpStr:
            return {"hibas": -1}
        for c in tmpStr:
            if c in tmp:
                tmp[c] += 1
            else:
                tmp[c] = 1

        most_frequent_character = max(tmp, key=tmp.get)
        
        return {most_frequent_character: tmp[most_frequent_character]}
    else:
        return {"hibas" : -1}
    
#print(karakter_modusz('aaabbc'))
#input1 = 'mondtam, fuss el, szedd a lábad, jól elbújtál, nem \n talállak '
#print(karakter_modusz(input1))
#print(karakter_modusz('megvárom veled a buszt uwu de csak ha szeretnéd owo'))

class Cipo:
    def __init__(self, marka, meret, ar = 10000):
        self.marka = marka
        self.meret = meret
        if ar > 0:
            self._ar = ar
        else:
            self._ar = 10000
        self.matricak = []

    @property
    def ar(self):
        return self._ar
    
    @ar.setter
    def ar(self, uj_ar):
        if type(uj_ar) is not int:
            self._ar = 10000
        elif uj_ar > 0:
            self._ar = uj_ar
        else:
            self._ar = 10000

    def matrica_hozzaadas(self, szoveg):
        if not isinstance(szoveg, str):
            raise ValueError("Hibas matrica!")
        tmpStr = szoveg[::2]
        if tmpStr not in self.matricak:
            self.matricak.append(tmpStr)
        
    
    def matrica_torles(self, szoveg):
        if not isinstance(szoveg, str):
            raise ValueError("Hibas matrica!")
        tmpStr = szoveg[::2]
        if tmpStr in self.matricak:
            self.matricak.remove(tmpStr)
    

    def __str__(self):
        if self.matricak:
            matrica_count = len(self.matricak)
            matrica_str = ', '.join(self.matricak)
            return f"Az uj {self.marka} markaju, EU {self.meret} meretu cipo ara jelenleg {self._ar} Ft. {matrica_count} db matrica van rajta.\nNev szerint: {matrica_str}."
        else:
            return f"Az uj {self.marka} markaju, EU {self.meret} meretu cipo ara jelenleg {self._ar} Ft es meg se lett meg sertve matricakkal."
        
    def __iadd__(self, other):
        if not isinstance(other, Cipo):
            raise ValueError("Hibas tipus!")
        
        for m in other.matricak:
            if m not in self.matricak:
                self.matricak.append(m)
        
        self._ar += int(other.ar * 0.7)
        return self
    
    def __eq__(self, other):
        if not isinstance(other, Cipo):
            raise ValueError("Hibas tipus!")
        return self.marka == other.marka and self.ar == other.ar
    
egy_cipo = Cipo("Nike", 35, 5000)
egy_masik_cipo = Cipo("Adidas", 36, 5005)
egy_cipo.ar = -1

egy_masik_cipo.matrica_hozzaadas("Valami")
egy_masik_cipo.matrica_hozzaadas("Kekw")

egy_cipo += egy_masik_cipo

print(egy_cipo) # Az uj Nike markaju cipo, EU 35 meretu cipo ara jelenleg
#13503 Ft. 2 db matrica van rajta.
#Nev szerint: Valami, Kekw.
print(egy_cipo == egy_masik_cipo) # False