date = input('Enter month (XX/XX/XX): ')
date = date.split('/')
date_day = int(date[0])
date_month = int(date[1])
date_year = int(date[2])

if date_day * date_month == date_year:
    print('Date is magic.')
else:
    print('Date is not magic.')
