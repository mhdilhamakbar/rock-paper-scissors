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

#Write your code below this line 👇
images = [rock, paper, scissors]
questions_user = input("Type '0' for rock,'1' for paper, '2' for scissors\n")
questions_user_2 = int(questions_user)
if  questions_user_2 >= 3 or questions_user_2 < 0:
  print("You typed invalid number")
else:
  print(images[questions_user_2])


  questions_user_2 = int(questions_user)
  questions_com = random.randint(0, 2)

  print(f"computer chose {questions_com}")
  print(images[questions_com])




  if questions_user_2 == 0 and questions_com == 2:
    print("You win")
  elif questions_com == 0 and questions_user_2 == 2:
    print("Computer win")
  elif questions_com > questions_user_2:
    print("Computer win")
  elif questions_user_2> questions_com:
    print("You win")
  elif questions_user_2 == questions_com:
    print("Draw")