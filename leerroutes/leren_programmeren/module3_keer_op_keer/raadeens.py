import random

score = 0                                 
for ronden in range(1,21):        #20 ronden
    num = random.randint(1,1000)  #random int
    for geraden in range(10):     #je mag 10 keer raden
        raden = int(input("Raad het getal tussen 1 en 1000  "))
        verschil = abs (num - raden)  #absolute value of, als het in de min gaat word het weer positief

        if raden == num:   #als het geraden is: break
            print("Geraden! Top!")
            score += 1
            break
        elif num > raden:
            print("Hoger!")
        elif raden > num:
            print("Lager!")
                
        if verschil <=20:
            print("Je bent heel warm!")
        elif verschil <=50:
            print("Je bent warm!")

    
    if num != raden:           #als je na 10 keer het nummer niet hebt geraden
        print(f"Je hebt het getal niet geraden! Het getal was {num}")
    if ronden == 20:
        print(f"Je hebt {ronden} rondes gespeeld! Je eindscore is {score}")

    again = input(f"Je score is nu {score}. Wil je nog een keer?  ")      #wil je nog een keer
    if again in ("No", "n","Nee","nee"):
        print(f"Je hebt {ronden} rondes gespeeld! Je eindscore is {score}")
        print("Tot later!")
        quit()


print(f"Je hebt {ronden} rondes gespeeld! Je eindscore is {score}")     




