#Adventure game
from ast import If
from operator import truediv
from queue import Empty


def main():
    
    
    
    
    from asyncore import loop
    from tkinter import END, N
    from threading import Event

    #hier word je naam gevraagd
    name = input("What is your name?")
    #uitleg voor de game
    print(f"Welcome to the Jungle {name}! In this game you will make your way through the")
    print("dangerous jungle in an attempt to find the hidden treasure.")
    Event().wait(3)


    print('''        
                           .=""_;=.
                       ,-"_,=""     `"=.
                       "=._o`"-._        `"=.
                           `"=._o`"=._      _`"=._                    
                                :=._o "=._."_.-="'"=.
                         __.--" , ; `"=._o." ,-"""-._ ".  
                      _._"  ,. .` ` `` ,  `"-._"-._   ".'
                      |o`"=._` , "` `; .". ,  "-._"-._; ;           
                      | ;`-.o`"=._; ." ` '`."\` . "-._ /
                      |o;    `"-.o`"=._``  '` " ,__.--o;
                      | ;     (#) `-.o `"=.`_.--"_o.-; ;
                      |o;._    "      `".o|o_.--"    ;o;
                       "=._o--._        ; | ;        ; ;
                            "=._o--._   ;o|o;     _._;o;
                                 "=._o._; | ;_.--"o.--"
                                      "=.o|o_.--""
    ''')


    print("You have a map to the treasure but it is not complete, so you'll have to search around until you find the treasure yourself.")

    #hier word er gevraagd of de user wil spelen
    while True:
        play = str(input("Are you ready to play? Y/N"))

        if play in ( "N" ,"n", "no" , "No") :
          print('''Till next time!
          ''')
          exit()
        
        elif play in ("Y", "y" ,"yes","Yes"):
          print('''
          Let's start the game!
          ''')
          break

        else:
            print('''Please enter a valid choice
            ''')
            continue
        

    Event().wait(2)
    #meer uitleg voor de game
    print('''
    To win the game you need to explore the jungle and find the treasure.
    You also need to make sure you dont die.
     ''')

    Event().wait(4)

   
    print('''
    Good luck on your adventure!
     ''')

    Event().wait(3)
    #je krijgt de keuze om water te drinken
    while True:

      answer = input("You're walking through The jungle when suddenly you find a small lake with muddy water. Take a sip of water? Y/N:")
      if answer in ("Y", "y" , "yes", "Yes"):
        print("You go take a sip of the muddy water. The water is poisonous. You die a painful death. Game Over")
        exit()

      elif answer in ("N", "n", "no", "No"):
        print("You continue walking")
        break

      else:
        print("please enter a valid choice!")
        continue

    Event().wait(1)  
    #je komt een slang tegen, je krijgt de keuze om te vechten of te rennen
    while True:  
      print(r'''\   
                     ---_ ......._-_--.
                    (|\ /      / /| \  \
                    /  /     .'  -=-'   `.
                  /  /    .'             )
                _/  /   .'        _.)   /
                / o   o        _.-' /  .'
                \          _.-'    / .'*|
                \______.-'//    .'.' \*|
                  \|  \ | //   .'.' _ |*|
                  `   \|//  .'.'_ _ _|*|
                    .  .// .'.' | _ _ \*|
                    \`-|\_/ /    \ _ _ \*\
                    `/'\__/      \ _ _ \*\
                    /^|            \ _ _ \*
                  '  `             \ _ _ \      
                                    \_
           ''')

      snake = str(input("As you walk around a big tree you come face to face with a snake! Run or fight the snake? Run/Fight:"))
      if snake in ("run", "r", "Run", "RUN"):
        print("You run away and escape the snake!")
        break
      
      if snake in ("Fight", "f", "fight", "FIGHT"):
        print("You try to fight the snake with your bare hands and get bitten. You die of the poison. Game Over!")
        exit()

      else:
        print("Please enter a valid choice!")
        continue

    #je vind een verlaten huisje met een deel van de map erin, als je naar binnen gaat kan je de game sneller winnen
    while True:
      print(r'''\
                                       ____
                   ____________________|  |_____
                  /______________________________\ 
                 /________________________________\  
                   ||___|___||||||||||||___|__|||     
                   ||___|___||||||||||||___|__|||        
                   ||||||||||||||||||||||||||||||

      ''')
      
      huisje = str(input("You continue on your path to find the treasure. You see an abandoned wooden house. Do you want to explore it? Y/N"))
      if huisje in ("Yes", "y" ,"YES", "yes", "Y"):
        print("You enter the house and find another piece of the map. Now you can get there faster!")
        print("You take the map with you and head back outside")

        #je krijgt de keuze om bananen te gaan halen
        fruit = str(input("when you're outside you see some bananas hanging on a tree. Do you want to climb the tree and grab the bananas? Y/N"))
        if fruit in ("Yes", "y" "YES", "yes", "Y"):
         print("You climb the tree to grab the fruit when you see a group of monkeys in front of you. They fight you for the bananas. You end up falling to your death. Game Over!")
         exit()
        #je krijgt een raadsel dat je op moet lossen, je krijgt 3 kansen
        if fruit in ("N", "n", "no", "No"):
          print("You continue on your way to the treasure and walk into a dark cave. There's a text on the wall:")
          print("Before Mount Everest was discovered, what was the highest mountain in the world?")
          riddle = str(input("Solve te riddle to win the game:"))
          if riddle in ("mount everest", "Mount Everest", "mount Everest", "Mount everest"):
            print("Congratulations you found the treasure and won the game!")
            print('''        
                           .=""_;=.
                       ,-"_,=""     `"=.
                       "=._o`"-._        `"=.
                           `"=._o`"=._      _`"=._                    
                                :=._o "=._."_.-="'"=.
                         __.--" , ; `"=._o." ,-"""-._ ".  
                      _._"  ,. .` ` `` ,  `"-._"-._   ".'
                      |o`"=._` , "` `; .". ,  "-._"-._; ;           
                      | ;`-.o`"=._; ." ` '`."\` . "-._ /
                      |o;    `"-.o`"=._``  '` " ,__.--o;
                      | ;     (#) `-.o `"=.`_.--"_o.-; ;
                      |o;._    "      `".o|o_.--"    ;o;
                       "=._o--._        ; | ;        ; ;
                            "=._o--._   ;o|o;     _._;o;
                                 "=._o._; | ;_.--"o.--"
                                      "=.o|o_.--""
    ''')
            exit()
          
          else:
            print("That isn't right. 2 more tries left!")
            print("Before Mount Everest was discovered, what was the highest mountain in the world?")
            riddle = str(input("Solve te riddle to win the game:"))
            if riddle in ("mount everest", "Mount Everest", "mount Everest", "Mount everest"):
              print("Congratulations you found the treasure and won the game!")
              print('''        
                           .=""_;=.
                       ,-"_,=""     `"=.
                       "=._o`"-._        `"=.
                           `"=._o`"=._      _`"=._                    
                                :=._o "=._."_.-="'"=.
                         __.--" , ; `"=._o." ,-"""-._ ".  
                      _._"  ,. .` ` `` ,  `"-._"-._   ".'
                      |o`"=._` , "` `; .". ,  "-._"-._; ;           
                      | ;`-.o`"=._; ." ` '`."\` . "-._ /
                      |o;    `"-.o`"=._``  '` " ,__.--o;
                      | ;     (#) `-.o `"=.`_.--"_o.-; ;
                      |o;._    "      `".o|o_.--"    ;o;
                       "=._o--._        ; | ;        ; ;
                            "=._o--._   ;o|o;     _._;o;
                                 "=._o._; | ;_.--"o.--"
                                      "=.o|o_.--""
    ''')
              exit()

            else:
              print("That isn't right. 1 more try left!")


              print("Before Mount Everest was discovered, what was the highest mountain in the world?")
            riddle = str(input("Solve te riddle to win the game:"))
            if riddle in ("mount everest", "Mount Everest", "mount Everest", "Mount everest"):
              print("Congratulations you found the treasure and won the game!")
              print('''        
                           .=""_;=.
                       ,-"_,=""     `"=.
                       "=._o`"-._        `"=.
                           `"=._o`"=._      _`"=._                    
                                :=._o "=._."_.-="'"=.
                         __.--" , ; `"=._o." ,-"""-._ ".  
                      _._"  ,. .` ` `` ,  `"-._"-._   ".'
                      |o`"=._` , "` `; .". ,  "-._"-._; ;           
                      | ;`-.o`"=._; ." ` '`."\` . "-._ /
                      |o;    `"-.o`"=._``  '` " ,__.--o;
                      | ;     (#) `-.o `"=.`_.--"_o.-; ;
                      |o;._    "      `".o|o_.--"    ;o;
                       "=._o--._        ; | ;        ; ;
                            "=._o--._   ;o|o;     _._;o;
                                 "=._o._; | ;_.--"o.--"
                                      "=.o|o_.--""
    ''')
              exit()

            else:
              print("That isn't right. No more tries left. Game Over!")
              exit()
            
       #als je het huisje beslist niet in te gaan kom je een leeuw tegen     
      if huisje in ("N", "n", "no", "No"):
        print("You walk past the house.")
        Event().wait(2)
        print(r'''\       
                                 .-.       .-.
                                (   \_.-._/   )
                                 \           /
                                 | __     __ |
                                 | \O\   /O/ |
                                  \  "   "  /
                                  /\_`-v-'_/\
                                 /  \._|_./  \
                                |    \___/    |
                                |             |
                                |             |
                                |   |     |   |
                      .ww.     _|   |     |   |_
                    .\WWW=    / |   |     |   | \
                    \WWW=    |  |   |     |   |  |
                    \WW=     |  |   |     |   |  |
                    ( (      |  |   \     /   |  |
                    \ \___.-'\  \   \   /   /  /
                      `-.__.-(...(...)---(...)...)
        ''')
        
        lion = str(input("You continue on your path when you come face to face with a lion. fight or run? Fight/Run"))
        if lion in ("Fight", "fight",):
          print("The tiger charges towards you. You grab a rock on the floor and manage to hurt him. You manage to escape and continue on your way")
          

          #je krijgt de keuze om bananen te halen
          fruit = str(input("You see some bananas hanging on a tree. Do you want to climb the tree and grab the bananas? Y/N"))
          if fruit in ("Yes", "y" ,"YES", "yes", "Y"):
            print("You climb the tree to grab the fruit when you see a group of monkeys in front of you. They fight you for the bananas. You end up falling to your death. Game Over!")
            exit()
            s
           #je krijgt hier een raadsel, je hebt 3 kansen
          if fruit in ("N", "n", "no", "No"):
            print("You continue on your way to the treasure and walk into a dark cave. There's a text on the wall:")
            print("Before Mount Everest was discovered, what was the highest mountain in the world?")
            riddle = str(input("Solve te riddle to win the game:"))
            if riddle in ("mount everest", "Mount Everest", "mount Everest", "Mount everest"):
              print("Congratulations you found the treasure and won the game!")
              print('''        
                           .=""_;=.
                       ,-"_,=""     `"=.
                       "=._o`"-._        `"=.
                           `"=._o`"=._      _`"=._                    
                                :=._o "=._."_.-="'"=.
                         __.--" , ; `"=._o." ,-"""-._ ".  
                      _._"  ,. .` ` `` ,  `"-._"-._   ".'
                      |o`"=._` , "` `; .". ,  "-._"-._; ;           
                      | ;`-.o`"=._; ." ` '`."\` . "-._ /
                      |o;    `"-.o`"=._``  '` " ,__.--o;
                      | ;     (#) `-.o `"=.`_.--"_o.-; ;
                      |o;._    "      `".o|o_.--"    ;o;
                       "=._o--._        ; | ;        ; ;
                            "=._o--._   ;o|o;     _._;o;
                                 "=._o._; | ;_.--"o.--"
                                      "=.o|o_.--""
    ''')
              exit()

            else:
              print("That isn't right. 2 more tries left!")
              print("Before Mount Everest was discovered, what was the highest mountain in the world?")
              riddle = str(input("Solve te riddle to win the game:"))
              if riddle in ("mount everest", "Mount Everest", "mount Everest", "Mount everest"):
                print("Congratulations you found the treasure and won the game!")
                print('''        
                           .=""_;=.
                       ,-"_,=""     `"=.
                       "=._o`"-._        `"=.
                           `"=._o`"=._      _`"=._                    
                                :=._o "=._."_.-="'"=.
                         __.--" , ; `"=._o." ,-"""-._ ".  
                      _._"  ,. .` ` `` ,  `"-._"-._   ".'
                      |o`"=._` , "` `; .". ,  "-._"-._; ;           
                      | ;`-.o`"=._; ." ` '`."\` . "-._ /
                      |o;    `"-.o`"=._``  '` " ,__.--o;
                      | ;     (#) `-.o `"=.`_.--"_o.-; ;
                      |o;._    "      `".o|o_.--"    ;o;
                       "=._o--._        ; | ;        ; ;
                            "=._o--._   ;o|o;     _._;o;
                                 "=._o._; | ;_.--"o.--"
                                      "=.o|o_.--""
    ''')
                exit()

              else:
                 print("That isn't right. 1 more try left!")
                 print("Before Mount Everest was discovered, what was the highest mountain in the world?")
                 riddle = str(input("Solve te riddle to win the game:"))
                 if riddle in ("mount everest", "Mount Everest", "mount Everest", "Mount everest"):
                  print("Congratulations you found the treasure and won the game!")
                  print('''        
                           .=""_;=.
                       ,-"_,=""     `"=.
                       "=._o`"-._        `"=.
                           `"=._o`"=._      _`"=._                    
                                :=._o "=._."_.-="'"=.
                         __.--" , ; `"=._o." ,-"""-._ ".  
                      _._"  ,. .` ` `` ,  `"-._"-._   ".'
                      |o`"=._` , "` `; .". ,  "-._"-._; ;           
                      | ;`-.o`"=._; ." ` '`."\` . "-._ /
                      |o;    `"-.o`"=._``  '` " ,__.--o;
                      | ;     (#) `-.o `"=.`_.--"_o.-; ;
                      |o;._    "      `".o|o_.--"    ;o;
                       "=._o--._        ; | ;        ; ;
                            "=._o--._   ;o|o;     _._;o;
                                 "=._o._; | ;_.--"o.--"
                                      "=.o|o_.--""
    ''')
                  exit()

                 else:
                  print("That isn't right. No more tries left. Game Over!")
                  exit()


          
        #als je met de leeuw probeert te vechten ben je game over
        if lion in ("Run", "run"):
          print("You try to run away. The lion is too fast and catches up with you. Game Over")
          break

      
      else:
        print("Please enter a valid answer")






     
        



    






      
        

    




    


  

    

   

    




    

  













main()