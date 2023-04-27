name=input('Please enter your name:')
print('Welcome to the dice game=>',name)
dice=input('ENTER d TO ROLL THE DICE:')
import random
value=random.randint(1,6)
while dice=='d':
    if value==1:
        print("The ROLLED OUTCOME IS",value)
        print(''' 
         ___________
        |           |
        |           |   
        |     0     |
        |           |
        |___________|''')
        break
    elif value==2:
        print("The ROLLED OUTCOME IS",value)
        print('''
         ___________
        |           |
        |           |   
        |    0 0    |
        |           |
        |___________|  ''')
        break
    elif value==3:
        print("The ROLLED OUTCOME IS",value)
        print('''
         ___________
        |           |
        |     0     |   
        |    0 0    |
        |           |
        |___________|     ''')
        break
    elif value==4:
        print("The ROLLED OUTCOME IS",value)
        print('''
         ___________
        |           |
        |    0 0    |   
        |    0 0    |
        |           |
        |___________|     ''')
        break
    elif value ==5:
        print("The ROLLED OUTCOME IS",value)
        print('''
         ___________
        |           |
        |   0    0  |   
        |      0    |
        |   0    0  |
        |___________|     ''')
        break
    elif value==6:
        print("The ROLLED OUTCOME IS",value)
        
        print('''
     ___________
    |           |
    |   0 0 0   |   
    |           |
    |   0 0 0   |
    |___________|            ''')
        break
                
else:
    print('please enter d to roll the dice')
                
                
                
