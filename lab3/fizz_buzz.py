import math
num = int(input('Enter the number of your want:'))
num_3 = num/3
num_5 = float(num/5)
whnum_3 = math.floor(num_3)
whnum_5 = math.floor(num_5)

if num_3 == whnum_3 and num_5 == whnum_5:
    print('fizz-Buzz')
elif num_5 == whnum_5:
    print('buzz')
elif num_3 == whnum_3:
    print('fizz')
else:
    print(num)

