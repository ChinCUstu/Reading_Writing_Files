length = float(input('Input the length of rectangle 1: '))
width = float(input('Input the width of rectangle 1: '))
length_2 = float(input('Input the length of rectangle 2: '))
width_2 = float(input('Input the width of rectangle 2: '))

area_1 = length * width
area_2 = length_2 * width_2

if area_1 > area_2:
    print('Rectangle 1 has a greater area.')
elif area_2 > area_1:
    print('Rectangle 2 has a greater area.')
else:
    print('Equal areas.')
