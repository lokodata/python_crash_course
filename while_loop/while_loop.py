message = ''

print("Enter 'quit' to exit the program.")
while message != 'quit':
    message = input("Enter desired toppings: ")
    if message != 'quit':
        print("Adding " + message + " to your pizza.")
    else:
        print("Exiting program.")

print()

active = True

while active:
    age = int(input('Enter your age: '))
    if age < 3:
        print('Your ticket is free.')
    elif age <= 12:
        print('Your ticket is $10.')
    else:
        print('Your ticket is $15.')
    active = False

print()

num_people = int(input('How many people are in your group? '))

while num_people != 0:
    age = int(input('Enter your age: '))
    if age < 3:
        print('Your ticket is free.')
    elif age <= 12:
        print('Your ticket is $10.')
    else:
        print('Your ticket is $15.')
    num_people -= 1

print()

while True:
    toppings = input('Enter desired toppings: ')
    if toppings != 'pineapple':
        print('Adding ' + toppings + ' to your pizza.')
        continue
    else:
        print('Sorry, we are out of pineapple.')
        break
