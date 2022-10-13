
# hoeveel m uitgraven? 
# hoeveel m3 afvoer?

# lengte = float(input("Hoe lang")) #meter
# breedte = float(input("Hoe breed")) #meter
# diepte = float(input("Hoe diep")) #meter


lengte = 8 
breedte = 3
diepte = 1.5

afvoeren = 32.50
uitgraven = 25
zwembadgrond = lengte * breedte * diepte

totaalafvoeren = afvoeren * zwembadgrond
totaaluitgraven = uitgraven * zwembadgrond
totaalprijs = totaaluitgraven + totaalafvoeren


print(f"Offerte voor een zwembad van 8 bij 3 bij 1,5 meter (inhoud:{zwembadgrond} m3)")
print(f"Afvoeren grond: {totaalafvoeren}Euro")
print(f"Uitgraven: {totaaluitgraven} Euro")
print(f"totaal {totaalprijs} Euro")

