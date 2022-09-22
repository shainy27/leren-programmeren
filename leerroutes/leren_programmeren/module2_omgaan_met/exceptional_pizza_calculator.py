from socket import getprotobyname
from ssl import ALERT_DESCRIPTION_CERTIFICATE_UNOBTAINABLE

small = 9.99
medium = 13.99
large = 17.99

print(f"Hallo! kies hier de afmeting van uw pizza. de prijzen zijn: Small ({small}), medium ({medium}),large ({large})")
score = +1

while score == 1:
    try:
        smallpizzas = int(input("Hoeveel small pizzas wilt u?:"))
        score =+2
    except:
        print("Voer een geldig antwoord in! Als u geen small pizzas wilt voer dan 0 in.")


while score == 2:
    try:
         mediumpizzas = int(input("Hoeveel medium pizzas wilt u?:"))  
         score =+3
    except:
        print("Voer een geldig antwoord in! Als u geen medium pizzas wilt voer dan 0 in.")


while score == 3:
    try:
        largepizzas = int(input("Hoeveel large pizzas wilt u?:")) 
        score =+ 4
    except:
        print("Voer een geldig antwoord in! Als u geen grote pizzas wilt voer dan 0 in.")



smallpizzaprijs = smallpizzas * small
mediumpizzaprijs = mediumpizzas  * medium
largepizzaprijs = largepizzas * large
totaalprijs = smallpizzaprijs + mediumpizzaprijs + largepizzaprijs

print("----------------------------------------------------") #dit is het bonnetje
print(f"{smallpizzas}  small pizzas  : {smallpizzaprijs}€")
print(f"{mediumpizzas} medium pizzas  : {mediumpizzaprijs}€")
print(f"{largepizzas}  large pizzas  : {largepizzaprijs}€")
print("                                                    ")
print(f"totaal           : {totaalprijs}€")
print("----------------------------------------------------")



















