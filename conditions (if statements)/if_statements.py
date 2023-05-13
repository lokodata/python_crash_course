alien_color = 'green'

if alien_color == 'green':
    print('You just earned 5 points!\n')

alien_color1 = 'red'
if alien_color1 == 'green':
    print('')

if alien_color == 'green':
    print('You just earned 5 points! for shooting the alien')
else:
    print('You just earned 10 points!')

print()

if alien_color1 == 'green':
    print('You just earned 5 points!')
elif alien_color1 == 'yellow':
    print('You just earned 10 points!')
else:
    print('You just earned 15 points!')

print()

age = 12

if age < 2:
    print('You are a baby')
elif age < 4:
    print('You are a toddler')
elif age < 13:
    print('You are a kid')
elif age < 20:
    print('You are a teenager')
elif age < 65:
    print('You are an adult')
else:
    print('You are an elder')

print()

favorite_fruits = ['apple', 'banana', 'orange']

if 'apple' in favorite_fruits:
    print('You really like apples!')
if 'banana' in favorite_fruits:
    print('You really like bananas!')
if 'orange' in favorite_fruits:
    print('You really like oranges!')
if 'grape' in favorite_fruits:
    print('You really like grapes!')
if 'watermelon' in favorite_fruits:
    print('You really like watermelons!')
