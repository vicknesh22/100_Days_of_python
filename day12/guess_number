#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
#############
import random
from logo import logo
print(logo)
print("\t\tWelcome to Guessing Game!!!")
print("\nThinking a number between 1 and 100")
R_NUM = random.randint(1,100)
print(R_NUM)
diff = input("\nChoose dificulty level easy or hard? : ")

if diff =="easy":
  retry = 10
  print(f"You have {retry} chances to find the number")
elif diff =="hard":
  retry = 5
  print(f"You have {retry} chances to find the number")
else:
  print("\nPlease follow the given options")

unum = int(input("\nGuess the number? : "))

#############

def findnum():
  global retry
  
  while retry != 0:
    unum = int(input("\nGuess the number? : "))
    
    if unum == R_NUM:
      print(f"You got it! The answer is {unum}")
    elif unum > R_NUM:
      retry -= 1
      print(f"\nThe guess is too high, you have {retry} attempts left.")
    elif unum < R_NUM:
      retry -= 1
      print(f"\nThe guess is too low, you have {retry} attempts left.")
  print(f"You have exahusted max attempts to find the number, correct ans is: {R_NUM}") 

  
findnum()
