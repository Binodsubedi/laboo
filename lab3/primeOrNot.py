import math

num = int(input('Enter the number to check:'))
if num<=3 and num>0:
    prime = True
else:
    divo1 = num/2
    divo = math.floor(divo1)
    rdevo = divo + 1
    for i in range (2, rdevo):
        remainder = num%i
        if remainder== 0:
            prime = False
            break
        else:
            prime = True
if prime == True:
    print('It is a prime number')
else:
    print('It is a non-prime number')
