
# hoeveel m uitgraven? 
# hoeveel m3 afvoer?




lengte = float(input("Hoe8 lang")) #meter
breedte = float(input("Hoe breed")) #meter
diepte = float(input("Hoe diep")) #meter
afstand = float(input("Wat is de afstand naar het zwembad?"))


zwembadgrond = lengte * breedte * diepte
vasteprijsklein = 100
vasteprijsgroot = 250


afvoeren = 32.50
uitgraven = 25

if (afstand < 50) and (zwembadgrond < 20): 
   voorrijkosten = 0
   voorrijkostentotaal = voorrijkosten + vasteprijsklein + zwembadgrond * 1.25
elif (afstand >= 50) and (zwembadgrond < 20):
   voorrijkosten = 0
   voorrijkostentotaal = voorrijkosten + vasteprijsklein + zwembadgrond * 1.15
elif (afstand < 50) and (zwembadgrond >= 20):
   voorrijkosten = 0
   voorrijkostentotaal = voorrijkosten + vasteprijsgroot + zwembadgrond * 2.15
elif (afstand >= 50) and (zwembadgrond >= 20):
  voorrijkosten = 0
  voorrijkostentotaal = voorrijkosten + vasteprijsgroot + zwembadgrond * 2.05



totaalafvoeren = afvoeren * zwembadgrond
totaaluitgraven = uitgraven * zwembadgrond
roundedafvoer = afvoeren
roundeduitgraven = totaalafvoeren
voorrijkosten = voorrijkostentotaal
totaalprijs = totaaluitgraven + totaalafvoeren + voorrijkostentotaal
roundtotaal = round(totaalprijs,2)

print(f"Offerte voor een zwembad van 8 bij 3 bij 1,5 meter (inhoud:{zwembadgrond} m3)")
print(f"Afvoeren grond: {totaalafvoeren}Euro")
print(f"Uitgraven: {totaaluitgraven} Euro")
print(f"Voorrijkosten: {voorrijkostentotaal}")
print(f"totaal {roundtotaal} Euro")

print(roundedafvoer)