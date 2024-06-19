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
import random
user_choice =int(input("what do you choose?type 0 for rock,1 for paper or 2 for scissors\n"))
if user_choice == 0:
    print("you choose rock"+" "+rock)
elif user_choice ==1:
    print("you choose paper"+" "+paper)
elif user_choice ==2:
    print("you choose scissors"+" "+scissors)
else:
    print("invalid input")
computer_choice =random.randint(0,2)
print("computer choose:")
if computer_choice == 0:
    print("rock" + rock)
elif computer_choice ==1:
    print("paper"+ paper)
elif computer_choice ==2:
    print(" scissors"+ scissors)
if user_choice =="0" and computer_choice ==2:
    print("you win")
elif user_choice =="2" and computer_choice ==1: 
    print("you win")
elif user_choice == "1"and computer_choice ==0:
    print("you win")
elif user_choice =="0" and computer_choice== 0:
    print("draw")
elif user_choice =="1" and computer_choice== 1:
    print("draw")
elif user_choice =='2'and computer_choice== 2:
    print("draw")
elif user_choice=='2'and computer_choice==0:
    print("you loose")
elif user_choice=='1'and computer_choice==2:
    print("you loose")
else:
    print("you loose")
    
