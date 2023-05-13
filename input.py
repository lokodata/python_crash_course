car = input('What kind of car? ')

print('Let me see if I can find you a ' + car.title() + '.')

print()

num_group = int(input('How many people are in your group? '))

if num_group > 8:
    print('You will have to wait for a table.')
else:
    print('Your table is ready.')

print()

num = int(input('Enter a number: '))
if num % 10 == 0:
    print('This number is a multiple of 10.')
else:
    print('This number is not a multiple of 10.')
