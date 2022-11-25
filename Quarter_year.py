MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December']
month = int(input("Enter a month as number(1 to 12): "))
if month == 1 or month == 2 or month == 3:
    print(f'{MONTHS[month - 1]} is in the first quarter.')
elif month == 5:
    print(f'{MONTHS[month - 1]} is in the second quarter.')
elif month == 7 or month == 8 or month == 9:
    print(f'{MONTHS[month - 1]} is in the third quarter.')
elif month == 11:
    print(f'{MONTHS[month - 1]} is in the fourth quarter.')
else:
    print('ERROR!')
