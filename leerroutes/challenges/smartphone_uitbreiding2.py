# prijs uitrekenen


# prijs uitrekenen

from operator import ipow
from tkinter.messagebox import askquestion


iphone = round(float(input("Hoeveel kost de Iphone 13?")))
samsung = round(float(input("Hoeveel kost de Samsung Galaxy S22?")))
asus = round(float(input("Hoeveel kost de Asus Zenfone 9?:")))

verschil= iphone - samsung #if iphone niet duurder dan 50 euro van samsung
verschil1= samsung - asus #if zenfone 100 euro goedkoper dan samsung
verschil2= iphone - asus #if zenfone 100 euro goedkoper dan Iphone


maxgetal= max(samsung , iphone , asus)
mingetal= min(samsung , iphone , asus)

def middle(samsung, iphone, zenFone) : 
    return min(max(samsung,iphone),max(iphone,asus),max(samsung,asus))


if iphone == maxgetal:
     print (f"de iphone is dus het duurste, de telefoon kost {iphone} euro")
elif samsung == maxgetal:
     print (f'de samsung is dus het duurste, de telefoon kost {samsung} euro ')
else:
     print (f' deZenFone is dus het duurste, de telefoon kost {asus} euro')

# goedkoopste  
()   
if iphone == mingetal:
     print (f"de iphone is dus het goedkoopste, de telefoon kost {iphone} euro")
     
elif samsung == mingetal:
     print (f'de samsung is dus het goedkoopste, de telefoon kost {samsung} euro ')
else:
     print (f'de ZenFone is dus het goedkoopste, de telefoon kost {asus} euro')

#als het gelijk is
()
if iphone == samsung and iphone == asus and samsung == asus:
     gelijk= print ('De prijzen zijn gelijk')
elif samsung == iphone:
     gelijk= print ('De samsung en iphone zijn gelijk')
elif samsung == asus:
     gelijk= print ('De samsung en zenFone zijn gelijk')
elif iphone == asus:
     gelijk= print ('De ZenFone en Iphone zijn gelijk')

#tussenin
()
if iphone == middle(samsung, iphone, asus):
     print (f"de iphone zit er tussenin met {iphone} euro")
elif samsung == middle(samsung, iphone, asus):
     print (f'de samsung zit er tussenin met {samsung} euro ')
else:
     print (f' de ZenFone zit er tussenin met {asus} euro')

#het advies
if samsung > 900 or iphone > 900 or asus > 900:
     print ("het advies is dus geen telefoon te kopen, ze zijn te duur!")
elif verschil1 >= 100 and verschil2 >= 100:
     print (f'het advies is dus om ZenFone te kopen. Deze is namelijk {verschil1} goedkoper dan samsung en {verschil2} goedkoper dan Iphone ')
elif verschil >= 50:
     print (f'"het advies is dus de Iphone te kopen. Deze is namelijk {verschil} goedkoper dan de samsung en {verschil2} goedkoper dan de Zenphone!"')
elif iphone == mingetal:
     print (f'"het advies is dus de iphone te kopen. Deze is namelijk {verschil} goedkoper dan de samsung en {verschil2} goedkoper dan de zenPhone"') 
elif samsung == mingetal:     
     print (f'"het advies is dus de samsung te kopen. Deze is namelijk {verschil} goedkoper dan de Iphone en {verschil1} goedkoper dan de zenPhone"') 










         



