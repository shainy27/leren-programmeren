import random

kleuren = ['rood', 'blauw', 'groen', 'geel', 'bruin']
zak = {}
aantal = int(input("Hoeveel M&M's wilt u in de zak doen? "))


for i in range(4): 
    value = random.randint(0,aantal)            #randint tussen 0 en aantal m&ms
    aantal -= value                             #trekt randint af van m&ms
    color = random.choice(kleuren)              # color = random kleur uit de lijst
    kleuren.remove(color)                       #haalt de random kleur uit de lijst
    zak[color] = value                          #bind de random kleur aan de value 


zak[kleuren[0]] = aantal                        # bind de laatste kleur aan de rest van de m&ms, 0 omdat er alleen een kleur nog in zit

print(f"Er zitten nu {zak} in de zak")