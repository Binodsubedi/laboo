enter = input('Enter the word you want:')
numbo = len(enter)
index = numbo
upper = 0
lower = 0
for i in range (numbo):
    index -= 1
    val = enter[index]
    upperval = enter[index].upper()
    lowerval = enter[index].lower()
    if val == upperval:
        upper += 1
    elif val == lowerval:
        lower += 1

print(f'The number of uppercase letters is {upper}')
print(f'The number of lowercase letters is {lower}')
