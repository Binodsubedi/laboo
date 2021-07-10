num1 = int(input('Enter your first number:'))
num2 = int(input('Enter the second number:'))
num3 = int(input('Enter the third number:'))
if num1>num2 and num1>num3:
    print(f'the number one {num1} is the largest')
elif num2>num1 and num2>num3:
    print(f'the number second {num2} is the highest')
else:
    print(f'the third {num3} is the way to go ')
    