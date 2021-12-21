import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("WELCOME TO MY NEW COOL GAME :) v1.0")
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

print("You chose:")

if user_input == 0:
  print(rock)
elif user_input == 1:
  print(paper)
elif user_input == 2:
  print(scissors)
else:
  print("Please restart and write a valide number: 0,1 or 2")


#Generating a random sequence of 3 integers
pc_input = (random.randint(0, 2))
print("Computer chose:\n")
if pc_input == 0:
  print(rock)
elif pc_input == 1:
  print(paper)
else:
  print(scissors)

#combination

if user_input == pc_input:
  print("DRAW.NOBODY WINS")
elif user_input > pc_input:
  if user_input == 2 and pc_input == 0:
    print("YOU LOSE! SORRY ;() ")
  else:
    print("YOU WIN CONGRATS")
elif pc_input > user_input:
  if pc_input == 2 and user_input == 0:
    print("YOU WIN CONGRATS")
  else:
    print("YOU LOSE! SORRY :(")
else:
  print("OPS something went wrong! Restart the game :)")