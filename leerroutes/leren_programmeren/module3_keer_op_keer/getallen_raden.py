import random

rondes = 0
score = 0
for ronden in range(20):
    rondes +=1
    num = random.randint(1,1000)
    for geraden in range(10):
        print(num)
        raden = int(input("Raad het getal tussen 1 en 1000  "))
        verschil = abs (num - raden)

        if num > raden:
            print("Hoger!")
        if raden > num:
            print("Lager!")
        elif raden == num:
            print("Geraden! Top!")
            score += 1
            break    
        
        if verschil <=20:
            print("Je bent heel warm!")
        elif verschil <=50:
            print("Je bent warm!")

    if num != raden:
        print("Je hebt het getal niet geraden!")
    if rondes == 20:
        print(f"Je hebt {rondes} rondes gespeeld! Je eindscore is {score}")

    again = input(f"Je score is nu {score}. Wil je nog een keer?")
    if again in ("No", "n","Nee","nee"):
        print(f"Je hebt {rondes} rondes gespeeld! Je eindscore is {score}")
        print("Tot later!")
        exit()


print(f"Je hebt {rondes} rondes gespeeld! Je eindscore is {score}")




