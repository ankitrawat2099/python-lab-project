name=input('please enter your name:')
print('welcome to the game:',name)
print('The Rules of the game is:\n1>rock beats scissor\n2>scissor beats paper\n3>paper beats rock')
print('The Game begins')

user_choice=input("enter your choice:")
choices=['rock','paper','scissor']
import random
computer_choice=random.choice(choices)
print('user choice is=',user_choice)
print('computer choice is=',computer_choice)


    
if computer_choice==user_choice:
    print('MATCH TIED')
elif user_choice=='rock':
    if computer_choice=='scissor':
        print('YOU WON')
    else:
        print('YOU LOST')
elif user_choice=='paper':
    if computer_choice=='scissor':
        print('YOU LOST')
    else:
        print("YOU WON")
elif user_choice=='scissor':
    if computer_choice=='paper':
        print('YOU WON')
    else:
        print('YOU LOST')

else:
    print('please enter the choice from rock,paper,scissor only')
