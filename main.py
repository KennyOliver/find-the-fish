'''
fishgame = [
  ["e", "e", "e"], 
  ["e", "e", "e"], 
  ["e", "e", "e"],
  ["e", "e", "e"]
  ]
'''
from colorama import init
from termcolor import colored
import random
#====================
def find_fish(): 
  print("<-- Find the Fish -->")
  print("Guess where the fishes are!")
  print("10 points per fish\n") 

  score = 0 #initialise score variable to zero
  pond = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

  repeat_range = random.randint(1,4)
  if repeat_range == 1:
    print(f"There is {repeat_range} fish!")
  else:
    print(f"There are {repeat_range} fishes!")
  
  for _ in range(repeat_range):
    rand_x = random.randint(0,3)
    rand_y = random.randint(0,2)
    pond[rand_x][rand_y] = "F"
    
    x_guess = int(input("Guess row (0 to 3)\t--> "))
    while x_guess not in range(0,3+1):
      x_guess = int(input("ROW must be between 0-3\t\t--> "))
    y_guess = int(input("Guess column (0 to 2) --> "))
    while y_guess not in range(0,2+1):
      y_guess = int(input("COLUMN must be between 0-2 --> "))
    
    print(f"Coords ({x_guess},{y_guess})")
    if pond[x_guess][y_guess] == "F":
      print("Well done - you found a fish!\n")
      score += 10
    else:
      print("No fish here!\n")

  print(f"Your score is {score}/{10*repeat_range}")
  print ("Thanks for playing - come back soon!")

  replay()
#====================
def replay():
  rerun = input("Would you like to play again? (Y or N) \n--> ").upper()
  while rerun not in ['Y','N']:
    rerun = input("Would you like to play again? (Y or N) \n--> ").upper()
  if rerun == 'Y':
    print("\n" * 3)
    find_fish()
#====================
# MAIN PRGOGRAM
find_fish()