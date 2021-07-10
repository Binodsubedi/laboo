Number = int(input('Enter the number of stars line:'))
def star(Number):
    num = 0
    hello = '*'
    for i in range (Number):
        num += 1
        print(num * hello)

star(Number)


