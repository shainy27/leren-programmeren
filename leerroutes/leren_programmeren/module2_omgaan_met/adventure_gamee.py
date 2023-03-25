from threading import Event
import sys, time
from adventure_game_art import *

def game_over():
    play_again = input("Do you want to play again? Y/N")
    if play_again in ["Y", "y", "yes", "Yes"]:
        return
    elif play_again in ["N", "n", "no", "No"]:
        print("Thanks for playing!")
        exit()
    else:
        print("Invalid input, please enter Y or N.")


def points(health,energy):
    print(f'''Your health and energy points are now:
      health: {health}
      Energy: {energy}   
      ''')
    
    if (health) <= 0 or (energy) <=0 :
          sprint("You don't have enough points to continue. Game over!")
          play_again = input("Do you want to play again? Y/N")
          if play_again in ("Y", "y", "yes", "Yes"):
            play_game()
          else:
            return False

def play_game():

    health = 3
    energy = 3


    name = input("What is your name?")

    # uitleg voor de game
    sprint(f"Welcome to the jungle {name}! In this game you will make your way through the")
    sprint("dangerous jungle in an attempt to find the hidden treasure. ")
    sprint("You also need to make sure your health and energy points dont run out! You start with 3 points.")

    while True:
        play = str(input("Are you ready to play? Y/N"))

        if play in ("N", "n", "no", "No"):
            print('''Till next time!
            ''')
            exit()

        elif play in ("Y", "y", "yes", "Yes"):
            sprint("Good luck on your adventure!")
            break

        else:
            print('''Please enter a valid choice
            ''')

    Event().wait(1)

    #Slang

    while True:
        print(slang)
        snake = input("As you start exploring the jungle you hear noises coming from behind you. It's a snake! Fight the snake or Run? Run/Fight:").lower()
        if snake in ("fight", "f"):
            print("You try to fight the snake with your bare hands and get bitten. You lose 2 health points!")
            health = health -2
            break

        elif snake in ("run", "r"):
            sprint("You run away and escape the snake! The running made you tired. You lose 2 energy points!")
            energy = energy - 2
            break

        else:
            print("Please enter a valid choice!")

    Event().wait(1)
    points(health,energy)
    Event().wait(1)

    while True:
        answer = input("You're walking through The jungle when suddenly you find a small lake with muddy water. Take a sip of water? Y/N:").lower()

        if answer in ("y","yes"):
            sprint("You take a sip of the muddy water. Why would you do that? You lose a health point!")
            health -=1
            break

        if answer in ("n", "no"):
            print("You continue walking.")
            break

        else:
            print("please enter a valid choice!")

    Event().wait(1)
    points(health,energy)
    Event().wait(1)


    max_health = 3
    max_energy = 3

    while True:
        print(huis) 
        huisje = input("You continue on your path to find the treasure. You see an abandoned wooden house. Do you want to explore it? Y/N")

        if huisje in ("y" ,"yes",):
            print("You enter the house and find another piece of the map. Now you can get there faster!")
            rest = input("You can stay the night to restore all your health and energy points. Stay the night?")

            if rest in ("yes", "y"):
                health = max_health
                energy = max_energy
                print("You stay the night, your energy and health points are back to", max_health, "!")
                print("You get up the next morning and continue on your journey")
                break
            
            if rest in ("n", "no"):
                print("You decide not to stay the night and continue on your journey") 
                print("When you get back outside you realize a spider has bitten you! You lose 2 health points!")
                health -= 2
                break
        
        else:
            break
                
        
    Event().wait(1)
    points(health,energy)
    Event().wait(1)


    while True:

        print(leeuw)  
        lion = str(input("You continue on your path when you come face to face with a lion. fight or run? Fight/Run")).lower()
        if lion in ("fight","f"):
            sprint("The tiger charges towards you. You grab a rock on the floor and manage to hurt him. You manage to escape and continue on your way")
            sprint("You lose an energy point!")
            energy -=1
            break
        
        if lion in ("run","r"):
            print("You try to run away. The lion is too fast and catches up with you. You get eaten alive. Game Over")
            game_over()

    Event().wait(1)
    points(health,energy)
    Event().wait(1)


    fruit = str(input("you see some bananas hanging on a tree. Do you want to climb the tree and grab the bananas? Y/N")).lower()
    if fruit in ("y", "yes"):
        sprint("You climb the tree to grab the fruit when you see a group of monkeys in front of you. They fight you for the bananas. You end up falling to your death. Game Over!")
        game_over()

    if fruit in ("n","no"):
        sprint("You continue walking")



    while True:      
            help = input("You keep walking and see an old tired man sitting on a tree trunk. Talk to him? Y/N").lower()
            if help in ("yes","y"):
                sprint("\'Hello there, I bet you're also looking for the treasure arent ya.\'")
                sprint("\'It's right over there in the cave. But to get to it you need to solve a riddle. I couldn't solve it, you should try your luck\'")
                Event().wait(1)
                treasure()


            if help in ("no","n"):
                swim = input("You walk past the stranger. You then find a small body of water. Take a swim? Y/N").lower()
                if swim in ("yes", "y"):
                    sprint("You get into the body of water to relax. Then you start to feel movement in the water. There's piranhas in the water!")
                    sprint("You try to get out but it's too late, you get attacked. Game over!")
                    game_over()

                if swim in ("no","n"):
                    sprint("You decide not to take a swim and continue walking.")
                    treasure()


                else:
                    print("Please enter a valid response!")
                    
            else:
                print("Please enter a valid response!")

play_game()








