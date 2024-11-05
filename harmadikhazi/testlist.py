list = [
    {
        'Tamas': {
            'eldobott_hogolyok': 4,
            'talalt': 1
        },
        'Ferenc': {
            'eldobott_hogolyok': 16,
            'talalt': 6,
            'fejtalalat': 1
        },
        'Csaba': {
            'eldobott_hogolyok': 28,
        }
    },
    {
        'Tamas': {
            'eldobott_hogolyok': 2,
            'talalt': 2
        },
        'Ferenc': {
            'eldobott_hogolyok': 3,
            'talalt': 2,
            'fejtalalat': 1
        },
        'Csaba': {
            'eldobott_hogolyok': 4,
            'talalt': 2,
            'fejtalalat': 1
        }
    }
]

def maximize_delivery_value(weights, values, capacity):
    # A súlyok és értékek száma
    n = len(weights)
    
    # DP táblázat inicializálása (n+1 sor, capacity+1 oszlop)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]