enter = input('Enter the word to reverse:')
value = len(enter)
unitdecr = value
#first method(easy_one)

print(enter[::-1])
# And the second one, more intutive.

for i in range (value):
    unitdecr -= 1
    print(enter[unitdecr], end= '')


