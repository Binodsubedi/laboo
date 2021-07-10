enter = input('Enter a word to check for palaindrome:')
enterreverse = enter[::-1]

if enter == enterreverse:
    print('Yes! it is a palaindrome')
else:
    print('It is not a palaindrome')