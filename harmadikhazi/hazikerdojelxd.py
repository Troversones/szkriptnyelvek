# Nev: Kis Bence Róbert
# Neptun: IFQA67
# h: h264560


def nyertes_korok(list1, list2):
    if len(list1) != len(list2) or not list1 or not list2:
        return -1
    
    countWins = 0

    for i in range(len(list1)):
        if list1[i] > list2[i]:
            countWins+=1

    return countWins

#print(nyertes_korok([30, 50, 10, 80, 100, 40], [60, 20, 10, 20, 30, 20]))
