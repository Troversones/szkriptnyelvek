szam = 5

if szam > 4:
    print("hehe")
elif szam < 4:
    print("haha")
else:
    print("kurva anyád")

while szam > 0:
    print(szam)
    szam -= 1

szoveg = "Trombitaréz"

for betu in szoveg:
    print(betu)


#range(mettől, meddig, inkrementálás mennyiség), range(meddig)
for i in range(5):
    print(i)

f = int("5")

f += 5

print(f)

def kek(szam):
    szam += 15
    print(szam)

kek(f)

