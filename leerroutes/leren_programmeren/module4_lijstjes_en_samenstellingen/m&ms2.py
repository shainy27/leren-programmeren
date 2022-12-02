import random

kleurMM = ['rood', 'blauw', 'groen', 'geel', 'bruin']
MMzak = {}
print("Er zitten nu nog 0 M&M's in de M&M zak. ")
hoeveelheidMM = int(input("Hoeveel M&M's wilt u in de zak doen? "))

for i in range(4): 
    value = random.randint(0,hoeveelheidMM)            # randint kiest getal tussen 0 en hoeveelheidMM
    hoeveelheidMM -= value                             # trekt random aantal MM van totaal af -> overig
    color = random.choice(kleurMM)                     # geeft een random kleur uit lijst
    kleurMM.remove(color)                              # haalt ^ weg uit lijst
    MMzak[color] = value                               # maakt nieuwe value om weer mee te starten en bindt value (aantal) aan kleur


MMzak[kleurMM[0]] = hoeveelheidMM                      # laatste/ overige kleur aan aantal binden

print(f"Er zitten nu {MMzak} in de zak")