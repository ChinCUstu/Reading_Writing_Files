GRAVITY = 9.8
mass = float(input('Enter the mass of an object: '))
weight = mass * GRAVITY
if weight > 500:
    print('Too heavy')
else:
    if weight < 100:
        print('Too light')
