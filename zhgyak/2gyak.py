# Nev: Kis Bence Róbert
# Neptun: IFQA67
# h: h264560

def minta_egyezesek(szotar, szotar2):
    if not isinstance(szotar, dict) or not isinstance(szotar2, dict):
        return

    if len(szotar) == 0 and len(szotar2) == 0:
        return 0
    elif len(szotar) == 0:
        return -1
    elif len(szotar2) == 0:
        return -1
    
    if set(szotar.keys()) != set(szotar2.keys()):
        return -1
    
    ret = sum(1 for t in szotar if szotar[t] == szotar2[t])

    return ret

szotar = {"10:00": 33}
szotar2 = {"10:00": 33, "11:30": 63, "13:00": 132}

print(minta_egyezesek(szotar,szotar2))

