# Nev: Kis Bence Róbert
# Neptun: IFQA67
# h: h264560

class Palack:
    def __init__(self, ital, max_urtartalom, jelenlegi_urtartalom = 1):
            self.ital = ital
            self.max_urtartalom = max_urtartalom
            self._jelenlegi_urtartalom = jelenlegi_urtartalom

    @property
    def jelenlegi_urtartalom(self):
          return self._jelenlegi_urtartalom
    
    @jelenlegi_urtartalom.setter
    def jelenlegi_urtartalom(self, value):
        if value > self.max_urtartalom:
            self._jelenlegi_urtartalom = self.max_urtartalom
        elif value == 0:
            self._jelenlegi_urtartalom = 0
            self.ital = None
        else:
            self._jelenlegi_urtartalom = value

    def suly(self):
        return self.max_urtartalom / 35 + self._jelenlegi_urtartalom
    
    def __str__(self):
        return f"Palack, benne levo ital: {self.ital}, jelenleg {self.jelenlegi_urtartalom} ml van benne, maximum {self.max_urtartalom} ml fer bele."
    
    def __eq__(self, other):
        return (self.ital == other.ital and 
                self.max_urtartalom == other.max_urtartalom and
                self.jelenlegi_urtartalom == other.jelenlegi_urtartalom)
    
    def __iadd__(self, other: 'Palack'):
        if self.ital == other.ital:
            return self
        elif self.jelenlegi_urtartalom == 0:
            self.ital = other.ital

        newUrtart = self.jelenlegi_urtartalom + other.jelenlegi_urtartalom
        self.jelenlegi_urtartalom = newUrtart

        if self.jelenlegi_urtartalom > self.max_urtartalom:
            self.jelenlegi_urtartalom = self.max_urtartalom
            self.ital = 'keverek'

        return self

class VisszavalthatoPalack(Palack):
    def __init__(self, ital, max_urtartalom, palackdij = 25, jelenlegi_urtartalom=1):
        super().__init__(ital, max_urtartalom, jelenlegi_urtartalom)
        self.palackdij = palackdij
        
    def __str__(self):
        return f"VisszavalthatoPalack, benne levo ital: {self.ital}, jelenleg {self.jelenlegi_urtartalom} ml van benne, maximum {self.max_urtartalom} ml fer bele."
    
class Rekesz:
    def __init__(self, max_teherbiras):
        self.max_teherbiras = max_teherbiras
        self.palackok = []

    def suly(self):
        return sum(p.suly() for p in self.palackok)
    
    def uj_palack(self, palack: Palack):
        if self.suly() + palack.suly() <= self.max_teherbiras: 
            self.palackok.append(palack)
    
    def osszes_penz(self):
        return sum(p.palackdij for p in self.palackok if isinstance(p, VisszavalthatoPalack))
    
#palack1 = Palack("víz", 1000)
#palack2 = VisszavalthatoPalack("üdítő", 1500)

#print(palack1)
#print(palack2)

#rekesz = Rekesz(max_teherbiras=100.0)
#rekesz.uj_palack(palack1)
#rekesz.uj_palack(palack2)

#print(f"Rekesz súlya: {rekesz.suly()} kg")
#print(f"Összes palackdíj: {rekesz.osszes_penz()} Ft")
#goofy ahh konstruktorok redvás nyelv máglyára vele