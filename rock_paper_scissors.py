
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

# user turn
choice=input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n')
choice=int(choice)
game=[rock,paper,scissors]
print(game[choice])   
# Computer turn

print('Computer chose:\n')
computer=random.randint(0,2)
print(game[computer])

#end statement
def end():
    if choice==computer:
        print('Its a tie')
    elif (choice==0 and computer==1) or ( choice==1 and computer==2) or  (choice==2 and computer==0) :
        print('You lose')    
    elif (choice==0 and computer==2) or (choice==1 and computer==0) or  (choice==2 and computer==1) :
        print('You win')
    else:
        print('Invalid number!')
        quit()
end()


