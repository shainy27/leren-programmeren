# prijs uitrekenen


# prijs uitrekenen

from operator import ipow
from tkinter.messagebox import askquestion


iphone = round(float(input("Hoeveel kost de Iphone 13?")))
samsung = round(float(input("Hoeveel kost de Samsung Galaxy S22?")))
asus = round(float(input("Hoeveel kost de Asus?:")))
verschil = round(float(iphone - samsung))



#als de iphone en samsung hoger dan 900 zijn print hij de voorkeur en eindigt het programma
if iphone and samsung >900:    
    print(f"De Samsung Galaxy S22 kost meer dan 900 Euro, de telefoon kost: {samsung} Euro")
    print(f"De Iphone 13 kost meer dan 900 Euro, de telefoon kost: {iphone} Euro")
    print("Het advies is dus geen telefoon te kopen, ze zijn te duur.")
    exit()


#als het verschil minder dan 50 is en de samsung duurder is print het programma de voorkeur en eindigt hij.
if verschil <50 and samsung > iphone:
    print(f"De Samsung galaxy S22 is het duurst, de telefoon kost: {samsung} Euro")
    print(f"De Iphone 13 is het goedkoopst, de telefoon kost: {iphone} Euro")
    print(f"Naar voorkeur is het advies om de iphone te kopen. Het verschil is namelijk maar {verschil} Euro")
    exit()

#als het verschil minder dan 50 is en de iphone duurder dan samsung is print het programma de voorkeur en eindigt hij
if verschil <50 and iphone > samsung:
    print(f"De Iphone 13 is het duurst, de telefoon kost: {iphone} Euro")
    print(f"De Samsung Galaxy S22 is het goedkoopst, de telefoon kost: {samsung} Euro")
    print(f"Naar voorkeur is het advies om de iphone te kopen. Het verschil is namelijk maar {verschil} Euro")
    exit()

#als de iphone duurder is dan de samsung print de programma de voorkeur en eindigt hij
if iphone > samsung:
    print(f"De Iphone 13 is het duurst, de telefoon kost: {iphone} Euro")
    print(f"De Samsung is het goedkoopst, de telefoon kost: {samsung} Euro")
    print(f"Het advies is dus de Samsung te kopen. Deze is namelijk {iphone - samsung} Euro goedkoper dan de Iphone 13.")
    exit()

#als de samsung duurder is dan de iphone print de programma de voorkeur en eindigt hij
if samsung > iphone:
    print(f"De Samsung galaxy S22 is het duurst, de telefoon kost: {samsung} Euro")
    print(f"De Iphone 13 is het goedkoopst, de telefoon kost: {iphone} Euro")
    print(f"Het advies is dus de Iphone te kopen. Deze is namelijk {samsung - iphone} Euro goedkoper dan de Samsung Galaxy S22.")
    exit()

#als de samsung en de iphone even duur zijn print de programma de voorkeur en eindight hij
elif samsung == iphone:
    print(f"De telefoons zijn even duur.")
    if iphone and samsung >900:
        print("Het advies is geen telefoon te kopen, ze zijn te duur.")
    else:
         print(f"Het advies is om bij voorkeur de Iphone 13 te kopen.")

