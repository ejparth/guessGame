#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import logo

print(logo.fig)

import random
print("Welcome to the number Guessing Game")
print("I'm thinking of a number between 1 and 100")
choice = int(input('''Select the difficulty\n
1 = Easy\n
2= Medium\n
3 = Hard\n\n'''))
List_difficulty = [10,7,5]
game_difficulty = List_difficulty[choice-1]
flag = False
print (f"You have {game_difficulty} attempts to guess the number")

number_to_guess = random.randint(1,100)

while not flag:
  

  if game_difficulty == 0:
    print("you exharusted the chances! YOU LOSE")
    flag = True
    continue
  guess_num = int(input("guess the number "))
  if guess_num > number_to_guess and game_difficulty!=0:
    print("your guess is too high")
    game_difficulty -=1
  elif guess_num < number_to_guess and game_difficulty!=0:
    print("your guess is too low")
    game_difficulty -=1
  elif guess_num == number_to_guess:
    print("you got the number")
    print("You won")
    flag = True
  
  
    