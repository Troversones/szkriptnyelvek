# Nev: Kis Bence Róbert
# Neptun: IFQA67
# h: h264560
    
class SemmiNemMaradtAKonyvtarban(Exception):
    def __init__(self):
        super().__init__('Minden könyv kiesett.')

class Konyv:
    def __init__(self, cim, oldalszam=100):
        self._cim = cim
        self._oldalszam = oldalszam

    @property
    def cim(self):
        return self._cim
    
    @cim.setter
    def cim(self, uj_cim):
        self._cim = uj_cim

    @property
    def oldalszam(self):
        return self._oldalszam

    @oldalszam.setter
    def oldalszam(self, uj_oldalszam):
        if type(uj_oldalszam) is int or uj_oldalszam > 0:
            self._oldalszam = uj_oldalszam
        else: 
            self._oldalszam = 100

class Kategoria:
    def __init__(self, nev, konyvek=None):
        self.nev = nev
        self._konyvek = konyvek if konyvek is not None else []

    def __iadd__(self, konyv):
        if not isinstance(konyv, Konyv):
            raise TypeError('A kategóriába csak könyvek kerülhetnek!')
        elif konyv._oldalszam < 100:
            raise ValueError('Csak megfelelő hosszúságú könyvek kerülhetnek be!')
        else:
            self._konyvek.append(konyv)
        return self
    
    @property
    def konyvek(self):
        return self._konyvek

def kiemelkedo_konyvek(lista):
    tmp = []

    for kategoria in lista:
        if len(kategoria.konyvek) >= 2:
            for konyv in kategoria.konyvek:
                if konyv.oldalszam >= 200:
                    tmp.append(konyv)
    return tmp

def statisztika(lista):
    kategoriak = {}

    for cim, oldalszam, nev in lista:
        konyv = Konyv(cim, oldalszam)
        if nev not in kategoriak:
            kategoriak[nev] = Kategoria(nev)
        kategoriak[nev] += konyv

    kiemelkedo_konyvek = kiemelkedo_konyvek(list(kategoriak.values()))

    if not kiemelkedo_konyvek:
        raise SemmiNemMaradtAKonyvtarban()

    return kiemelkedo_konyvek