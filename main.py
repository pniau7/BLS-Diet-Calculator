# This project is meant to help people reading Michael Matthews' Bigger, Leaner, Stronger
# do their calories calculation and distribution.

from BLS_Aux import *
from datetime import datetime as dt
from os import path

unit = {'MKS': {'pweight': 'kilograms', 'mweight': 'grams', 'height': 'centimeters', 'dec': 0},
        'IPS': {'pweight': 'pounds', 'mweight': 'ounces', 'height': 'inches', 'dec': 2}}
conv = {'MKS': {'pweight': 1, 'mweight': 1, 'height': 1},
        'IPS': {'pweight': 1 / 2.20462, 'mweight': 1 / 0.035274, 'height': 1 / 0.393701}}

title()
print('''This script is meant to help people reading Michael Matthews' dieting book 
Bigger, Leaner, Stronger calculating their calories and macronutrients distribution.\n\n''')
print('''First, choose a unit system.

[1] - Kilograms, grams and centimeters
[2] - Pounds, ounces and inches
''')
opt = readOpt('Choose option 1 or 2: ')
if opt == 1:
    sys = 'MKS'
else:
    sys = 'IPS'

title()
print('''You want me to calculate your distribution based on your:

[1] - Age, height and weight
[2] - Total daily energy expenditure (TDEE)
''')
opt = readOpt('Choose option 1 or 2: ')

if opt == 1:
    title()
    print('''Let\'s calculate your Basal Metabolic Rate (BMR), which gives you an idea of how much
    energy your body approximately spends at rest.\n''')
    print('Let me know the following information.')
    height = readFloat('height', f'Your height in {unit[sys]["height"]}: ')
    weight = readFloat('weight', f'Your weight in {unit[sys]["pweight"]}: ')
    age = readFloat('age', 'Your age in years: ')

    BMR = 10 * weight * conv[sys]['pweight'] + 6.25 * height * conv[sys]['height'] - (age - 1) * 5

    print(f'Alright! Your BMR is {BMR:.0f} calories.')
    pause()

    title()
    print(f'''Your BMR is {BMR:.0f} calories. We now need to calculate your Total Daily Energy Expenditure (TDEE),
    which tells approximately the total amount of energy you spend daily, including exercises.\n''')

    while True:
        try:
            hours = float(input('For this, I need to know how many hours of activity you do per week: '))
            if hours > 0:
                break
            else:
                print('Type a valid amount of hours!')
        except (TypeError, ValueError):
            print('Type a valid amount of hours!')
        except KeyboardInterrupt:
            print('User ended the program.')
            exit()
        except:
            print('Unexpected error. Exiting the program.')
            exit()

    mult = 0.07023*hours + 1.12636
    TDEE = BMR*mult
    print(f'Great! Your TDEE is approximately {TDEE:.0f} calories.')
    pause()
elif opt == 2:
    BMR = 0
    title()
    print('Sure enough.')
    TDEE = readFloat('TDEE', 'Let me know your TDEE in calories: ')


title()
c_lean = 0.40 * 0.75 * TDEE / 4 / conv[sys]['mweight']
p_lean = 0.40 * 0.75 * TDEE / 4 / conv[sys]['mweight']
f_lean = 0.20 * 0.75 * TDEE / 9 / conv[sys]['mweight']
c_main = 0.45 * TDEE / 4 / conv[sys]['mweight']
p_main = 0.30 * TDEE / 4 / conv[sys]['mweight']
f_main = 0.25 * TDEE / 9 / conv[sys]['mweight']
c_bulk = 0.55 * 1.1 * TDEE / 4 / conv[sys]['mweight']
p_bulk = 0.25 * 1.1 * TDEE / 4 / conv[sys]['mweight']
f_bulk = 0.20 * 1.1 * TDEE / 9 / conv[sys]['mweight']
dec = unit[sys]['dec']

print(f'''Your BMR is {BMR:.0f} calories, and your TDEE is {TDEE:.0f} calories.
According to the book, if you want to lose fat, maintain or gain muscle, you should follow the
cutting, maintaining or bulking calorie intake and distribution, respectively.\n''')
print('They are:')
table = f'''{"":<17}{"Cutting":<16}{"Maintaining":<16}{"Bulking":<16}
Calorie intake
{"Total:":<17}{0.75*TDEE:<16.0f}{TDEE:<16.0f}{1.1*TDEE:<14.0f}{"calories":>5}

Macronutrients distribution
{"Carbohydrates:":<17}{c_lean:<16.{dec}f}{c_main:<16.{dec}f}{c_bulk:<14.{dec}f}{unit[sys]["mweight"]:>5}
{"Proteins:":<17}{p_lean:<16.{dec}f}{p_main:<16.{dec}f}{p_bulk:<14.{dec}f}{unit[sys]["mweight"]:>5}
{"Fats:":<17}{f_lean:<16.{dec}f}{f_main:<16.{dec}f}{f_bulk:<14.{dec}f}{unit[sys]["mweight"]:>5}
'''
print(table)
if opt == 1:
    person = f'Age = {age} years\nWeight = {weight} {unit[sys]["pweight"]}\nHeight = {height} {unit[sys]["height"]}\n\n'
else:
    person = ''
date = f'Created on: {dt.today().day:02}/{dt.today().month:02}/{dt.today().year:02}' \
       f' - {dt.today().hour:02}:{dt.today().minute:02}\n\n'

out = readYN('Would you like to export these results? [Y/N]: ')
pathname = 'BLS_Diet.txt'

if out == 'Y':
    if not read(pathname):
        create(pathname)
        write(pathname, 'wt', date + person + table)
    else:
        overw = readYN(f'{pathname} already exists.\nWould you like to overwrite previous diets? [Y/N]: ')
        if overw == 'Y':
            writeopt = 'wt'
            write(pathname, writeopt, date + person + table)
        elif overw == 'N':
            writeopt = 'at+'
            write(pathname, writeopt, '\n' + '-'*71 + '\n' + date + person + table)
print('Program finished.')
pause()
