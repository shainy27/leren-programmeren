# prijs uitrekenen

iphone = float(input("Hoeveel kost de Iphone 13?"))
samsung = float(input("Hoeveel kost de Samsung Galaxy S22?"))

if iphone > samsung:
    print(f"De Iphone 13 is het duurst, de telefoon kost: {iphone} Euro")
    print(f"De Samsung is het goedkoopst, de telefoon kost: {samsung} Euro")
    print(f"Het advies is dus de Samsung te kopen. Deze is namelijk {iphone - samsung} Euro goedkoper dan de Iphone 13.")

if samsung > iphone:
    print(f"De Samsung galaxy S22 is het duurst, de telefoon kost: {samsung} Euro")
    print(f"De Iphone 13 is het goedkoopst, de telefoon kost: {iphone} Euro")
    print(f"Het advies is dus de Iphone te kopen. Deze is namelijk {samsung - iphone} Euro goedkoper dan de Samsung Galaxy S22.")

elif samsung == iphone:
    print(f"De telefoons zijn even duur.")
    print(f"Het advies is om bij voorkeur de Iphone 13 te kopen.")