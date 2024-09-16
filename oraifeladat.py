#elso/masodik feladat

szam = 30
szoveg = "Trombitaréz"
word = "tégla"

def ennyire_akad_be_a_lemez(szam, szoveg):
    while szam > 0:
        if szam % 3 == 0: 
            szam -= 1
        elif word in szoveg:
            szam -= 1
        elif szoveg.isnumeric():
            szam -= 1
        else:
            print(szam,".",szoveg)
            szam -= 1

ennyire_akad_be_a_lemez(szam,szoveg)

#harmadik feladat

szoveg2 = ""

def vicc(szoveg):
    for i in range(len(szoveg)):
        if i % 2 != 0:
            szoveg2 += szoveg[i].lower()
        else:
            szoveg2 += szoveg[i].upper()

print(szoveg2)

        
