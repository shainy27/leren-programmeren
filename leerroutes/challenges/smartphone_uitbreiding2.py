# prijs uitrekenen

from operator import ipow
from tkinter import END





iphone = float(input("Hoeveel kost de Iphone 13?:"))
samsung = float(input("Hoeveel kost de Samsung Galaxy S22?:"))
asus = float(input("Hoeveel kost de Asus Zenfone 9?:"))



while True:

    if iphone > samsung and iphone > asus:
        print(f"De Iphone 13 is het duurst, de telefoon kost: {iphone} Euro")
        if iphone and samsung and asus >900:
            print("Het advies is dus geen telefoon te kopen, ze zijn te duur.")
            exit()
        if asus > samsung:
            print("samsung goedkoopst")
            print("asus ertussenin")
            print("Het advies is dus de samsung te kopen deze is namelijk")
        elif samsung > asus:
            print("asus goedkoopst")
            print("samsung ertussenin")
            print("Het advies is dus de asus te kopen deze is namelijk")

        if iphone and samsung and asus >900:
            print("Het advies is dus geen telefoon te kopen, ze zijn te duur.")
        else: 
            print(f"Het advies is dus de Samsung te kopen. Deze is namelijk {iphone - samsung} Euro goedkoper dan de Iphone 13. En {asus - samsung} Euro goedkoper dan de Asus")

    if samsung > iphone and samsung > asus:
        print(f"De Samsung galaxy S22 is het duurst, de telefoon kost: {samsung} Euro")
        print(f"De Iphone 13 is het goedkoopst, de telefoon kost: {iphone} Euro")
        if iphone and samsung >900:
            print("Het advies is dus geen telefoon te kopen, ze zijn te duur.")
        else:
            print(f"Het advies is dus de Iphone te kopen. Deze is namelijk {samsung - iphone} Euro goedkoper dan de Samsung Galaxy S22.")

    elif samsung == iphone == asus:
        print(f"De telefoons zijn even duur.")
        if iphone and samsung and asus >900:
            print("Het advies is dus geen telefoon te kopen, ze zijn te duur.")
        else:
            print(f"Het advies is om bij voorkeur de Iphone 13 te kopen.")
            break

