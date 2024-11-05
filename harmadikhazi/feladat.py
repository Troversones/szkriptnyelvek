# Nev: Kis Bence Róbert
# Neptun: IFQA67
# h: h264560

def hogolyo_csata(list):
    results = {}
 
    for rd in list:
        for p, d in rd.items():
            if p not in results:
                results[p] = {
                    'eldobott_hogolyok': 0,
                    'talalt': 0,
                    'fejtalalat': 0
                }
            results[p]['eldobott_hogolyok'] += d.get('eldobott_hogolyok', 0)
            results[p]['talalt'] += d.get('talalt', 0)
            results[p]['fejtalalat'] += d.get('fejtalalat', 0)

    return results

def hogolyo_pontossag(list):
    for p, d in list.items():
        totTh = d['eldobott_hogolyok']
        totHi = d['talalt']
        if totTh > 0:
            d['pontossag'] = totHi / totTh
        else:
            d['pontossag'] = 0.0

    return list

def hogolyo_piros_lap(list):
    rcp = []

    for p, d in list.items():
        totTh = d['eldobott_hogolyok']
        totHi = d['talalt']
        totHe = d['fejtalalat']
        if totTh > 0:
            acc = totHi / totTh
            heRa = totHe / totTh
            if acc >= 0.7 and heRa >= 0.5:
                rcp.append(p)

    return rcp

#test_1 = hogolyo_csata(list)
#print("Statisztika: ",test_1)

#test_2 = hogolyo_pontossag(test_1)
#print("Pontosság: ", test_2)

#test_3 = hogolyo_piros_lap(test_2)
#print("Piroslap: ", test_3)

#feladatban lévő minta input lett használva (*trademark)
#NO MULTI LINE COMMENT XDDDDDDDD MODERN LANGUAGE BTW