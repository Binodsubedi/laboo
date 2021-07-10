enter = input('Enter the text for even index order print:')
num = len(enter)
index = -1
indexlim = num -1
diff = (num-1) - 2
#easy peasy method
print(enter[1::2])
# A bit lengthy one
for i in range (num):
    index += 2

    if diff < 2:
        break
    if index> indexlim:
        break
    print(enter[index], end='')