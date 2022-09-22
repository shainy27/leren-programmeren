#Adventure game
from operator import truediv
from queue import Empty


def main():
    
    
    
    
    from asyncore import loop
    from tkinter import END, N
    from threading import Event


    name = input("What is your name?")

    print(f'''Welcome to the Jungle {name}! In this game you will make your way through the''')
    print("dangerous jungle in an attempt to find the hidden treasure.")


    while True:
        play = str(input("Are you ready to play? Y/N"))

        if play in ( "N" ,"n", "no") :
          print('''Till next time!
          ''')
          exit()
        

        elif play in ("Y", "y" ,"yes"):
          print('''
          Let's start the game!
          ''')
          break

        else:
            print('''Please enter a valid choice
            ''')
            continue
        

    Event().wait(3)

    print('''
    To win the game you need to explore the jungle and find the treasure.
    You also need to make sure you dont die.
     ''')

    Event().wait(4)

   
    print('''
    Good luck on your adventure!
     ''')

    Event().wait(3)

    print('''
    You're walking through the jungle and find a blue backpack lying on the floor. it might come in handy, you decide to take it with you.
    This is now your inventory
    ''')
    




    

  













main()