
# Libraries to Import
import sys
import time
import random
import os 

# Welcome Text
wstr="Welcome To"
centr=wstr.center(70)
print("\n",centr)

#Hangman figure, with each body part adding up
HANGMAN = (
"""
-----
|   |
|
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   O
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   O
|  -+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   O
| /-+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   O
| /-+-\ 
|
|
|
|
|
--------
""",
"""
-----
|   |
|   O
| /-+-\ 
|   | 
|
|
|
|
--------
""",
"""
-----
|   |
|   O
| /-+-\ 
|   | 
|   | 
|
|
|
--------
""",
"""
-----
|   |
|   O
| /-+-\ 
|   | 
|   | 
|  |
|
|
--------
""",
"""
-----
|   |
|   O
| /-+-\ 
|   | 
|   | 
|  | 
|  | 
|
--------
""",
"""
-----
|   |
|   O
| /-+-\ 
|   | 
|   | 
|  | | 
|  | 
|
--------
""",
"""
-----
|   |
|   O
| /-+-\ 
|   | 
|   | 
|  | | 
|  | | 
|
--------
""")

#Game information/help
def info():
  print('Welcome to Hangman! A word will be chosen at random and',
               'you must try to guess the word correctly letter by letter',
               'before you run out of attempts. Good luck!\n')
  print('Please select a game mode (1, 2 or 3):')


# Print HANGMAN
hang="HANGMAN"
nil=""
mid=nil.rjust(28)
print(mid, end=" ")
for i in range (0, 7):
    print(hang[i], end=" ")
    time.sleep(0.35)
print("\n")

#Primary game function
def play_game():

  #Calling to capture player information
  ask_info()

  #Calling to ask player a game mode
  ask_mode()

  
def ask_info():
  print("Please enter your name")
  Pname=input()

  #Checks if the file exists
  if os.path.exists('C:\\hangman')== True:

      #Checks if its a new player or a returning player
      gameFile=open('C:\\hangman\\PlayerInfo.txt','r')

      #Loop to check new/returning player 
      while True:
          line=gameFile.readline()
    
          #Writes the name of new player
          if Pname in line : 
              gameFile.close()
              print("Welcome back", Pname, "\n")
              break
              ask_mode()
            
          
          #Prints welcome back for returning player 
          else:
            gameFile=open('C:\\hangman\\PlayerInfo.txt','a')
            gameFile.write(Pname)
            gameFile.close()
            print("\n Greetings", Pname, "\n")
            break

  #Makes new file if it does not exists      
  else:
      os.makedirs('C:\\hangman')
      gameFile=open('C:\\hangman\\PlayerInfo.txt','w')
      gameFile.write(Pname)
      gameFile.close()
      print("\n Greetings", Pname, "\n")

    

# Function to ask the game mode
def ask_mode():
  
  mode="Game Mode Selection "
  hlp="Press 4 for help"
  
  print(mode)
  print("\n Please select a game mode (1, 2 or 3): \n")
  print("1. Animals/ Birds")
  print("2. Countries")
  print("3. Fruits \n")
  print(hlp.rjust(40))
  
  select=input()
  
  #loop for selection of game mode
  while select != '1' or select != '2' or select != '3':
    
    if select == '1':
      animals()
      break
    elif select == '2':
      country()
      break
    elif select == '3':
      fruits()
      break
    elif select == '4':
        info()
        select=input()
        continue
    else:
      print("Enter a correct option (1, 2 or 3):")
      select=input()
  
#Game mode 1
def animals():

  #Loop to add a seperation line
  for i in range (0, 40):
    print("x+",end="")
    time.sleep(0.03)

  #String for hint
  hinT=["""**Also considered as the second king of the Jungle**""", """**Walks very slowly, swims pretty fast**""",
        """**Colorful and can even speak your name**""", """**Looks dumb but can ruin your can window with its poop**""",
        """**Pretty long neck**""", """**This dog can laugh !**""", """**Is this a mammal or a bird ?**""", """**Big guy with a great memory**"""]

  #String for random words
  aniwords=["tiger", "turtle", "parrot", "pigeon", "girrafe", "hyena", "platypus", "eagle", "elephant", "rabbit"]
  chosen_word = random.choice(aniwords).lower()

  #Loop and condition to store a hint relevant to the random word selected
  for x in range (8):
    if chosen_word == aniwords[x]:
      hint = hinT[x]
    else:
      continue

  player_guess = None # will hold the players guess
  guessed_letters = [] # a list of letters guessed so far
  word_guessed = []

  #Display the number of blanks according to the random  word
  for x in range (8):
    if chosen_word == aniwords[x]:
      hint = hinT[x]
    else:
      continue

  player_guess = None # will hold the players guess
  guessed_letters = [] # a list of letters guessed so far
  word_guessed = []
  
  #Display the number of blanks according to the random  word
  for letter in chosen_word:
      word_guessed.append("-")
  joined_word = None

#Refering and printing the global Hangman variable
  print(HANGMAN[0])
 
#number of attemptes
  attempts = len(HANGMAN) - 1


  #Loop for the number of inputs a player gets
  while (attempts != 0 and "-" in word_guessed):

      #inserts the updated value of attempts in the placeholders
      print(("\nYou have {} attempts remaining").format(attempts))
      joined_word = "".join(word_guessed)
      print(joined_word)

      hinth="**Press '4' for hint**"
      print(hinth.rjust(80))

      try:
        #Add player's input
          player_guess = str(input("\nPlease select a letter between A-Z" + "\n>")).lower()
      except: # check valid input
          print("That is not valid input. Please try again.")
          continue                
      else: 
          if not player_guess.isalpha() and player_guess != "4": # check the input is a letter. Also checks an input has been made.
              print("That is not a letter. Please try again.")
              continue
           #Checks if player asked for a hint
          elif player_guess == "4":
              print("\n")
              print(hint)
              time.sleep(2.3)
              continue
          elif len(player_guess) > 1 and player_guess != "exit": # check the input is only one letter
              print("That is more than one letter. Please try again.")
              continue
          elif player_guess == "exit": # checks if player asked to exit the game

              while True:
                print("\n Are you sure you want to exit the current game mode (y/n) ? \n")
                ans=input()
                if ans=="Y" or ans=="y":
                  ask_mode()
                elif ans=="N" or ans=="n":
                  attempts=attempts+1
                  break
                else:
                  print("\n Please enter 'Y' or 'N' \n")
                
          elif player_guess in guessed_letters: # check it letter hasn't been guessed already
              print("You have already guessed that letter. Please try again.")
              continue
          else:
              pass

      guessed_letters.append(player_guess)

      for letter in range(len(chosen_word)):
          if player_guess == chosen_word[letter]:
              word_guessed[letter] = player_guess # replace all letters in the chosen word that match the players guess

      if player_guess not in chosen_word:
          attempts = attempts- 1
          print(HANGMAN[(len(HANGMAN) - 1) - attempts]) #Reduces attempt and prints figure if wrong guess


  if "-" not in word_guessed: # no blanks remaining
      print("\nCongratulations!", chosen_word, "was the word")
      time.sleep(1)

      #Ask again to play
      while True:
        print("\n Wanna play again (Y/N)? \n ")
        again= input()
        if again == 'y' or again == 'Y':
            print ('\n')
            ask_mode()
        elif again == 'n' or again == 'N':
            sys.exit()
        else:
            print("Please enter Yes(Y) or No(N)")

          
  else: # loop must have ended because attempts reached 0
      print("\nUnlucky! The word was", chosen_word)
      time.sleep(1)

      #Ask again to play
      while True:
        print("\n Wanna play again (Y/N)? \n ")
        again= input()
        if again == 'y' or again == 'Y':
          print ('\n')
          ask_mode()
        elif again == 'n' or again == 'N':
          sys.exit()
        else:
          print("Please enter Yes(Y) or No(N)")

#Game mode 2
def fruits():
  #Loop to add a seperation line
  for i in range (0, 40):
    print("x+",end="")
    time.sleep(0.03)
  
  #String for hint
  hinT=["""**Doctor is afraid of this fruit**""", """**Is always being compared with apples**""",
        """**Name will remind you of your papa**""", """**Monkey's first love**""",
        """**bunch of small ovals**""", """**colour and shape like someone's rear**""", """**Don't lick it raw !**""", """**have a whole army inside, rhymes with 'Grenade'**"""]
  
  #String for random words
  fruwords=["apple", "orange", "papaya", "banana", "grapes", "peach", "lemon", "pomegranate"]
  chosen_word = random.choice(fruwords).lower()
  
  #Loop and condition to store a hint relevant to the random word selected
  for x in range (8):
    if chosen_word == fruwords[x]:
      hint = hinT[x]
    else:
      continue
  player_guess = None # will hold the players guess
  guessed_letters = [] # a list of letters guessed so far
  word_guessed = []
  
  #Display the number of blanks according to the random  word
  for letter in chosen_word:
      word_guessed.append("-")
  joined_word = None

#Refering and printing the global Hangman variable
  print(HANGMAN[0])
 
#number of attemptes
  attempts = len(HANGMAN) - 1


  #Loop for the number of inputs a player gets
  while (attempts != 0 and "-" in word_guessed):

      #inserts the updated value of attempts in the placeholders
      print(("\nYou have {} attempts remaining").format(attempts))
      joined_word = "".join(word_guessed)
      print(joined_word)

      hinth="**Press '4' for hint**"
      print(hinth.rjust(80))

      try:
        #Add player's input
          player_guess = str(input("\nPlease select a letter between A-Z" + "\n>")).lower()
      except: # check valid input
          print("That is not valid input. Please try again.")
          continue                
      else: 
          if not player_guess.isalpha() and player_guess != "4": # check the input is a letter. Also checks an input has been made.
              print("That is not a letter. Please try again.")
              continue
           #Checks if player asked for a hint
          elif player_guess == "4":
              print("\n")
              print(hint)
              time.sleep(2.3)
              continue
          elif len(player_guess) > 1 and player_guess != "exit": # check the input is only one letter
              print("That is more than one letter. Please try again.")
              continue
          # checks if player asked to exit the game
          elif player_guess == "exit": 

              while True:
                print("\n Are you sure you want to exit the current game mode (y/n) ? \n")
                ans=input()
                if ans=="Y" or ans=="y":
                  ask_mode()
                elif ans=="N" or ans=="n":
                  attempts=attempts+1
                  break
                else:
                  print("\n Please enter 'Y' or 'N' \n")
                  
          elif player_guess in guessed_letters: # check it letter hasn't been guessed already
              print("You have already guessed that letter. Please try again.")
              continue
          else:
              pass

      guessed_letters.append(player_guess)

      for letter in range(len(chosen_word)):
          if player_guess == chosen_word[letter]:
              word_guessed[letter] = player_guess # replace all letters in the chosen word that match the players guess

      if player_guess not in chosen_word:
          attempts -= 1
          print(HANGMAN[(len(HANGMAN) - 1) - attempts]) #Reduces attempt and prints figure if wrong guess

  if "-" not in word_guessed: # no blanks remaining
        print("\nYup!", chosen_word, "was the word")
        time.sleep(1)

        #Ask again to play
        while True:
          print("\n Wanna play again (Y/N) ? \n ")
          again= input()
          if again == 'y' or again == 'Y':
            print ('\n')
            ask_mode()
          elif again == 'n' or again == 'N':
            sys.exit()
          else:
            print("Please enter Yes(Y) or No(N)")
          
  else: # loop must have ended because attempts reached 0
      print("\nNope! The word was", chosen_word)
      time.sleep(1)
      
      #Ask player to pay again
      while True:
        print("\n Wanna play again (Y/N)? \n ")
        again= input()
        if again == 'y' or again == 'Y':
          print ('\n')
          ask_mode()
        elif again == 'n' or again == 'N':
          sys.exit()
        else:
          print("Please enter Yes(Y) or No(N)")

#Game mode 3
def country():

  #Loop to add a seperation line
    for i in range (0, 40):
      print("x+",end="")
      time.sleep(0.03)
    
    #String for hint
    hinT=["""**This country has Taj Mahal**""", """**This country has a virus**""",
        """**This country has Statue of Liberty **""", """**This country is the second largest in the world**""",
        """**This country is famous for it's Pizzas**""", """**This country has a Queen**""", """**This country is a continent itself**""", """**This country has the tallest building in the world**"""]

    #String for random words
    countwords=["india", "china", "america", "canada", "italy", "england", "australia", "dubai"]
    chosen_word = random.choice(countwords).lower()
    
    #Loop and condition to store a hint relevant to the random word selected
    for x in range (8):
      if chosen_word == countwords[x]:
        hint = hinT[x]
      else:
        continue
    player_guess = None # will hold the players guess
    guessed_letters = [] # a list of letters guessed so far
    word_guessed = []

    #Display the number of blanks according to the random  word
    for letter in chosen_word:
        word_guessed.append("-")
    joined_word = None

    #Refering and printing the global Hangman variable
    print(HANGMAN[0])

    #number of attemptes
    attempts = len(HANGMAN) - 1

    #Loop for the number of inputs a player gets
    while (attempts != 0 and "-" in word_guessed):

        #inserts the updated value of attempts in the placeholders
        print(("\nYou have {} attempts remaining").format(attempts))
        joined_word = "".join(word_guessed)
        print(joined_word)

        hinth="**Press '4' for hint**"
        print(hinth.rjust(80))

        try:
            #Add player's input
            player_guess = str(input("\nPlease select a letter between A-Z" + "\n> ")).lower()
        except: # check valid input
            print("That is not valid input. Please try again.")
            continue                
        else: 
            if not player_guess.isalpha() and player_guess != "4": # check the input is a letter. Also checks an input has been made.
                print("That is not a letter. Please try again.")
                continue
            
            #Checks if player asked for a hint
            elif player_guess == "4":
              print("\n")
              print(hint)
              time.sleep(2.3)
              continue
            elif len(player_guess) > 1 and player_guess != "exit": # check the input is only one letter
              print("That is more than one letter. Please try again.")
              continue

            # checks if player asked to exit the game
            elif player_guess == "exit": 
              while True:
                print("\n Are you sure you want to exit the current game mode (y/n) ? \n")
                ans=input()
                if ans=="Y" or ans=="y":
                  ask_mode()
                elif ans=="N" or ans=="n":
                  attempts=attempts+1
                  break
                else:
                  print("\n Please enter 'Y' or 'N' \n")
                
            elif player_guess in guessed_letters: # check it letter hasn't been guessed already
                print("You have already guessed that letter. Please try again.")
                continue
            else:
                pass

        guessed_letters.append(player_guess)

        for letter in range(len(chosen_word)):
            if player_guess == chosen_word[letter]:
                word_guessed[letter] = player_guess # replace all letters in the chosen word that match the players guess

        if player_guess not in chosen_word:
            attempts -= 1
            print(HANGMAN[(len(HANGMAN) - 1) - attempts]) #Reduces attempt and prints figure if wrong guess

    if "-" not in word_guessed: # no blanks remaining
        print("\nYup!", chosen_word, "was the word")
        time.sleep(1)

        #Ask player to pay again
        while True:
          print("\n Wanna play again (Y/N)? \n ")
          again= input()
          if again == 'y' or again == 'Y':
            print ('\n')
            ask_mode()
          elif again == 'n' or again == 'N':
            sys.exit()
          else:
            print("Please enter Yes(Y) or No(N)")
          
    else: # loop must have ended because attempts reached 0
        print("\nNope! The word was", chosen_word)
        time.sleep(1)

        #Ask again to play
        while True:
          print("\n Wanna play again (Y/N) ? \n ")
          again= input()
          if again == 'y' or again == 'Y':
            print ('\n')
            ask_mode()
          elif again == 'n' or again == 'N':
            sys.exit()
          else:
            print("Please enter Yes(Y) or No(N)")

play_game()
