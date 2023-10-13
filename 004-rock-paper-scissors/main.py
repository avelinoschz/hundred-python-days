import random

rock_image = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper_image = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors_image = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
options = [rock_image, paper_image, scissors_image]

rock = 0
paper = 1
scissors = 2

draw = "It's a draw"
win = 'You win!'
lose = 'You lose'

player = int(
    input(
        'What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'
    ))

computer = random.randint(0, 2)

if player >= 3:
  print('invalid number choice')
  
else:
  if player == computer:
      result = draw

  elif player == rock:
      if computer == scissors:
          result = win
      elif computer == paper:
          result = lose

  elif player == paper:
      if computer == rock:
          result = win
      elif computer == scissors:
          result = lose

  elif player == scissors:
      if computer == paper:
          result = win
      elif computer == rock:
          result = lose

  message = f'''
  {options[player]}
  Computer chose:
  {options[computer]}
  {result}
  '''
  
  print(message)
