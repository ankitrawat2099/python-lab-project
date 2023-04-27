import random
value=random.random()
digit=int(input('Enter the digit 4/6 of which otp you want:'))
otp=str(value)[-digit:]
print(otp)
