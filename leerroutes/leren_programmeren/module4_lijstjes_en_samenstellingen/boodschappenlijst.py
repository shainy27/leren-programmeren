
winkelmand = []  #lege list
doorgaan = True
while doorgaan: 
    getal = True
    verder = True
    item = input("Voeg een item toe aan uw winkelmand  ").capitalize()  #voeg een item toe aan de lijst

    while getal:
        try:
            aantal = int(input("Hoeveel van deze item wilt u hebben?  "))     #hoeveel van de item moet op de lijst staan
            getal = False
        except:
            print("Voer een geldig getal in!")

    winkelmand.insert(0,f"{aantal}x {item}")   #insert naar de lijst

    while verder:
        door = input("Wilt u nog een item toevoegen?  ").lower()   #nog een item toevoegen?
        if door in "nee":
            doorgaan = False
            verder = False
        if door in "ja":
            verder = False
            
print("")
print("-[Boodschappenlijst]-")   #print boodschappenlijst
print("")
list(map(print, winkelmand))






