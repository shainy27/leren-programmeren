
from fruitmand import fruitmand
kleuren = []                                               #lege list
for fruit in range(len(fruitmand)):                        
    if fruitmand[fruit]['color'] not in kleuren:           #als het nog niet in de list zit zet hij hem in de list
        kleuren.append(fruitmand[fruit]['color'])

while True:
    kleurkiezen = input(f"Welke kleur? Kies uit de kleuren: {kleuren}")          #kies een kleur
    if kleurkiezen not in kleuren:
        print("Deze kleur zit niet in de fruitmand")
    else:
        print(f"De kleur {kleurkiezen} zit in de fruitmand")
        break

ronde = 0
nietronde = 0

for fruit in range(len(fruitmand)):                    
    if fruitmand[fruit]['round'] == True and fruitmand[fruit]['color'] == kleurkiezen:    # als de fruit rond is en dezelfde kleur +=1 ronde
        ronde += 1
    elif fruitmand[fruit]['round'] == False and fruitmand[fruit]['color'] == kleurkiezen:  #als je fruit niet rond is maar wel dezelfde kleur += niet ronde
        nietronde += 1 

verschilrond = abs(ronde - nietronde)  

if ronde > nietronde:
    print(f'Er zijn {verschilrond} meer ronde vruchten dan niet ronde vruchten in de kleur {kleurkiezen}')
elif ronde < nietronde: 
    print(f"Er zijn {verschilrond} minder ronde vruchten dan niet ronde vruchten in de kleur {kleurkiezen}")
else: 
    print(f"Er zijn {verschilrond} ronde vruchten en {verschilrond} niet ronde vruchten in de kleur {kleurkiezen}")


            







    