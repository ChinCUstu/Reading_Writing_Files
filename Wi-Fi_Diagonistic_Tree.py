print('Reboot the computer and try to connect.')
print('Did that fix the problem?: ')
option = input("'yes' or 'no': ")
option = option.lower()

if option == 'no':
    print('Reboot the router and try to connect.')
    print('Did that fix the problem?: ')
    option = input("'yes' or 'no': ")
    if option == 'no':
        print('Make sure the cables between the router & modem are plugged in firmly')
        print('Did that fix the problem?: ')
        option = input("'yes' or 'no': ")
        if option == 'no':
            print('Move the router to a new location and try to connect')
            print('Did that fix the problem?: ')
            option = input("'yes' or 'no': ")
            if option == 'no':
                print('Get a new router.')
else:
    exit(0)
