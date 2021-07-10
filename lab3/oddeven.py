import math
def filter(lim):
    number = lim
    numbo = -1
    for i in range (number):
        numbo +=1
        div_num= numbo/2
        print(numbo)
        whdiv_num = math.floor(div_num)
        if whdiv_num == div_num:
            print('even')
        else:
            print('odd')

lim = int(input('Enter the limit:'))
filter(lim)