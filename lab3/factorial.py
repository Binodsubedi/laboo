import math
num1 = int(input('Enter the first number:'))
num2 = int(input('Enter the second number:'))
def factorial():
    div = num1/num2
    whdiv = math.floor(div)
    if div == whdiv:
        print('The remainder is 0')
    else:
        mulval = div - whdiv
        value = mulval * num2
        intvalue = math.floor(value)
        print(f'the value of remainder is {intvalue}')
factorial()
