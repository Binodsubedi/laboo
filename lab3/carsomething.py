hello = True
started = 0
while hello ==True:
    given = input('Enter the process:')

    if given.lower() == 'start':
        if started == 1:
            print('Already started')
        else:
            print('The vehicle has started')
            started = 1

    elif given.lower() == 'stop':
        print('It is stoped')
        break
    else:
        print('invalid')

