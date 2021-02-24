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
  print("Welcome to the find the fish game - guess where the fish is!")
  print("You score 10 points if you find a fish\n") 

  pond = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]] #set up the 2 D array

  rand_x_first = random.randint(0,3)
  rand_y_first = random.randint(0,2)
  rand_x_second = random.randint(0,3)
  rand_y_second = random.randint(0,2)

  pond[rand_x_first][rand_y_first] = "F"
  pond[rand_x_second][rand_y_second] = "F"

  score = 0 #initialise score variable to zero

  row = int(input("Guess the row number (0 to 3)\t--> "))
  column = int(input("Guess the column number (0 to 2)\t--> "))

  if pond[row][column] == "F":
    print(colored("well done - you have found a fish!\n", 'green'))
    score = score + 10
  else:
    print(" :) No fish here!\n")

  print(f"Your score is {score}")
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