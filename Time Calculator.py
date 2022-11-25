day = hour = minute = 0
seconds = int(input('Enter number of seconds: '))
if seconds >= 60:
    minute = seconds / 60
if seconds >= 3_600:
    hour = seconds / 3_600
    minute = seconds / 60
if seconds >= 86_400:
    day = seconds / 86_400
    hour = seconds / 3600
    minute = seconds / 60
print(f'{seconds} is {day}d, {hour}hrs,{minute}min, {seconds}s')
