#








from operator import truediv


naam = input("Wat is uw naam?")

man = input("Bent u een man en heeft u een snor langer dan 10 cm? Ja/Nee")
if man == "ja":
  sollicitatie = True
else:
    vrouw = input("Bent u een vrouw met rood krulhaar van 20 cm? Ja/Nee")
    if vrouw == "ja":
     sollicitatie = True
  


ervaring = int(input("Hoeveel jaar praktijkervaring heeft u met dierendressuur"))
if ervaring >4:
  heeft_ervaring = True
else:
    ervaring = int(input("Hoeveel jaren ervaring heeft u met..."))
    if ervaring >4:
     heeft_ervaring = True
    else: 
      ervaring = int(input("hoeveel jaren ervaring heeft u met..."))
      if ervaring >5:
        heeft_ervaring = True


diploma = input("Bent u in bezit van een diploma MBO4 ondernemen? Ja/Nee")
if diploma == "ja":
  heeft_diploma = True

rijbewijs = input("Bent u in bezit van een geldig vrachtwagen rijbewijs? Ja/Nee")
if rijbewijs == "ja":
 heeft_rijbewijs = True

lengte = int(input("Wat is uw lengte in cm?"))
if lengte >150:
  goede_lengte = True


gewicht = int(input("Hoeveel weegt u?"))
if gewicht >= 90: goede_gewicht = True

certificaat = input("Heeft u de certificaat Overleven met gevaarlijk personeel? Ja/Nee")
if certificaat == "ja":
  heeft_certificaat = True



sollicitatie_punten = sollicitatie and heeft_ervaring and heeft_diploma and heeft_rijbewijs and goede_lengte and goede_gewicht and heeft_certificaat
if sollicitatie_punten:
  print("U komt in aanmerking voor een sollicitatiegesprek!")

else:
    print("Helaas komt U niet in aanmerking voor een sollicitatiegesprek")


 

















  





