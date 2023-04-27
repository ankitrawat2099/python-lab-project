name=input('Please enter your name:')
print('Welcome to the game=>',name)
attempt=10
import random
lower_range=int(input('enter the lower range you want to given:'))
upper_range=int(input('enter the upper range you want to given:'))
number_range=random.randint(lower_range,upper_range)
while attempt:
    user_number=int(input(f'Guess the number betweeen {lower_range} and {upper_range}:'))
    if user_number>number_range:
        print('Guess number is large\nGuess again!')
    elif user_number<number_range:
        print('Guess number is small\nGuess again!')
    else:
        print('YOU WON')
        break
    attempt-=1
else:
    print('YOU LOSS')
