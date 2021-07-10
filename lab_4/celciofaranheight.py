unit = int(input('1 for c to f and 2 for f to c:'))
value = int(input('Enter the value for conversion:'))

if unit == 1:
    conversion1 = value
    conversion1 = (conversion1 * 1.8)+32
    print(f'{conversion1} FAHRENHEIT')
elif unit == 2:
    conversion2 = value
    conversion2 -= 32
    mulval = conversion2* 0.5556
    print(f'{mulval} CELCIUS')
else:
    print('invalid input')