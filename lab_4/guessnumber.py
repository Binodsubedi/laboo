import random
random = random.randint(1, 9)
attempt = True
while attempt == True:
    volvo = int(input('Enter you guess:'))

    if random == volvo:
        print('Correct guess')
        break
    else:
        print('try again')
