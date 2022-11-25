height = float(input('Enter your height: '))
weight = float(input('Enter your weight: '))

body_mass_index = weight * 703 / (height ** 2)

if 18.5 <= body_mass_index <= 25:
    print('Optimal Weight')
elif body_mass_index > 25:
    print('Overweight')
else:
    print('Underweight')
