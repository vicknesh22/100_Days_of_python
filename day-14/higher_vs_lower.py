from game_data import data
from art import logo,vs
import random

######### printing comapre A ##########
print(logo)
random_dic_list = random.choice(data)
random_dic_list_two = random.choice(data)
actual = ""
def compare(random_dic_list, random_dic_list_two):
  
  print(f"\nCompare A: {random_dic_list['name']}, {random_dic_list['description']}, from {random_dic_list['country']}")
  a = random_dic_list['follower_count']
  
  print(vs)

 
  print(f"\nAgainst B: {random_dic_list_two['name']}, {random_dic_list_two['description']}, from {random_dic_list_two['country']}")

  b = random_dic_list_two['follower_count']
  global actual
  
  if a > b:
    actual = "A"
    return actual 
  elif b > a:
    actual = "B"
    
    return actual 



################# user input #########

compare(random_dic_list, random_dic_list_two)
user = input("\nWho has more followers? Type 'A' or 'B':  ")
score = 0
game_over = 0

while game_over == 0:
  if actual == user:
    score += 1
    print(f"\nYou're right! Current score: {score}.")
    if actual == "A":
      random_dic_list = random_dic_list
      random_dic_list_two = random.choice(data)
    elif actual == "B":
      random_dic_list = random_dic_list_two
      random_dic_list_two = random.choice(data)
    compare(random_dic_list, random_dic_list_two)
    user = input("\nWho has more followers? Type 'A' or 'B':  ")
  elif actual != user:
    game_over = 1
    print(f"\nSorry, that's wrong. Final score: {score}")
    
   
