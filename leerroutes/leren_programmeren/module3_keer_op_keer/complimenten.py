from operator import truediv
from random import random
import random
import _random


naam = input("wat is je naam")
hoeveel_complimenten = int(input("hoeveel complimenten"))


# lijst randomchoice
# randint if



for x in range(hoeveel_complimenten):
    while True:
        rand = random.randint(1,4)
        if rand == 1:
            print(f"Je bent echt cool {naam}")
            vorige_rand = 1
        elif rand == 2:
            print(f"Je bent gewelding {naam}")
            vorige_rand = 2
        elif rand == 3:
            print(f"Je bent mooi {naam}")
            vorige_rand = 3
        if rand == 4:
            print(f"Je bent fantastisch {naam}")
            vorige_rand = 4
