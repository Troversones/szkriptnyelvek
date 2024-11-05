# Nev: Kis Bence Róbert
# Neptun: IFQA67
# h: h264560

def exponens(szoveg: str, szorzo: int = 1, kitevo: int = 1) -> str:
    szoveg = str(szoveg)
    
    if kitevo < 1:
        tmp = szorzo
    else:
        tmp = szorzo ** kitevo
    
    return szoveg * tmp

print(exponens("fasz",25))
print(exponens("levél"))

def kodolo(szoveg):
    if isinstance(szoveg, str):
        szoveg = szoveg.replace('a','#').replace('e','##').replace('i','###').replace('o','####').replace('u','#####')
        return szoveg
    else:
        return szoveg
    
print(kodolo("alma"))
print(kodolo("gumiabroncs"))