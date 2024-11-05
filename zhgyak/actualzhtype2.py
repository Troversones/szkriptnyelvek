def palindrom_ido(idopont):
    # Ellenőrizzük, hogy a bemenet sztring-e
    if not isinstance(idopont, str):
        return False

    # Az időpont szétválasztása óra és perc részekre
    try:
        ora, perc = idopont.split(":")
    except ValueError:
        return False  # Ha a formátum nem megfelelő (pl. nincs kettőspont), visszatér hamissal
    
    # Ellenőrizzük, hogy az óra és perc számjegyekből áll-e és megfelelő tartományban van-e
    if not (ora.isdigit() and perc.isdigit()):
        return False

    ora = int(ora)
    perc = int(perc)
    
    if not (0 <= ora <= 23 and 0 <= perc <= 59):
        return False

    # Az óra és perc értékek formázása kétjegyűre
    ora_str = f"{ora:02}"
    perc_str = f"{perc:02}"

    # Ellenőrizzük, hogy az óra visszafordítva megegyezik-e a perccel
    return ora_str == perc_str[::-1]


class Fesztival:
    def __init__(self, nev="nincs", ferohely=1000):
        self.nev = nev
        self.ferohely = ferohely
        self.latogatok = 0
        self.biztonsagi_orok = []

    def biztonsagi_felvetel(self, jelentkezo):
        # Ellenőrizzük, hogy a jelentkező rendelkezik-e a szükséges képességgel
        if 'orzes_vedes' not in jelentkezo or not jelentkezo['orzes_vedes']:
            return False

        # Ellenőrizzük, hogy van-e hely a fesztiválon
        if self.latogatok + len(self.biztonsagi_orok) >= self.ferohely:
            raise Exception("Nincs hely")

        # Hozzáadjuk a biztonsági őrt
        self.biztonsagi_orok.append(jelentkezo['nev'])
        return True

    def biztonsag_rendben(self):
        # Ellenőrizzük, hogy megfelelő számú biztonsági őr van-e
        if self.latogatok < 20:
            return True
        return len(self.biztonsagi_orok) >= (self.latogatok // 20)

    def __iadd__(self, other):
        # Ellenőrizzük, hogy a másik objektum is Fesztival típusú-e
        if isinstance(other, Fesztival):
            # Összeadjuk a látogatók számát és a biztonsági őrök listáját
            self.latogatok += other.latogatok
            self.biztonsagi_orok.extend(other.biztonsagi_orok)
            self.ferohely += other.ferohely
        return self

    def __str__(self):
        return f"A {self.nev} fesztivalon jelenleg {self.latogatok} latogato van."

    @property
    def bentlevok(self):
        # Visszaadjuk a bent lévők számát (látogatók + biztonsági őrök)
        return self.latogatok + len(self.biztonsagi_orok)

    @bentlevok.setter
    def bentlevok(self, value):
        # Beállítjuk a látogatók számát
        self.latogatok = value - len(self.biztonsagi_orok)
        # Ellenőrizzük, hogy a látogatók száma nem haladja meg a maximális férőhelyet
        if self.latogatok < 0:
            self.latogatok = 0
        elif self.latogatok + len(self.biztonsagi_orok) > self.ferohely:
            self.latogatok = self.ferohely - len(self.biztonsagi_orok)

# Tesztelés
fesztival = Fesztival("SummerFest")
print(fesztival.nev)  # "SummerFest"
print(fesztival.ferohely)  # 1000
print(fesztival.latogatok)  # 0
print(fesztival.biztonsagi_orok)  # []

fesztival.biztonsagi_felvetel({"nev": "Kovacs Bela", "orzes_vedes": True})
print(fesztival.biztonsagi_orok)  # ["Kovacs Bela"]
print(fesztival.biztonsag_rendben())  # False

fesztival2 = Fesztival("RockFest", 500)
fesztival2.latogatok = 300
fesztival2.biztonsagi_felvetel({"nev": "Nagy Istvan", "orzes_vedes": True})

fesztival += fesztival2
print(fesztival2)  # "A RockFest fesztivalon jelenleg 300 latogato van."

fesztival2.bentlevok = 310
print(fesztival2.latogatok)  # 309
fesztival2.bentlevok = 1000
print(fesztival2.latogatok)  # 499