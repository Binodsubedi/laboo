Number = int(input('Enter the number:'))
process = True
def summul(number):
    num_3 = 0
    num_5 = 0
    summ = 0;
    while process == True:
        num_3 += 1
        num_5 += 1
        num3mul = num_3 *3
        num5mul = num_5 *5
        num3diff = number - num3mul
        num5diff = number - num5mul
        if num3mul<=number and num5mul<=number:
            if num3mul== num5mul:
                summ += num3mul
            else:
                summ += num3mul + num5mul
        elif num3mul<=number and num5diff<5:
            summ += num3mul
        elif num3diff<3 and num5diff<5:
            break


    return summ
print(summul(Number))







