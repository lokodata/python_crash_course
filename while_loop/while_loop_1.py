sandwich_orders = ['tuna', 'pastrami',
                   'chicken', 'pastrami', 'beef', 'pastrami']
finished_sandwiches = []

while sandwich_orders:
    current_orders = sandwich_orders.pop()
    print("I made your " + current_orders.title() + " sandwich")
    finished_sandwiches.append(current_orders)

print("\nAll sandwiches are made: ")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title() + " sandwich")

print()

print("The deli has run out of pastrami.")
while 'pastrami' in finished_sandwiches:
    finished_sandwiches.remove('pastrami')

print("\nAll sandwiches are made: ")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title() + " sandwich")

print()

dream_vacations = {}

responding = True

while responding:
    user = input("What is your name? ")
    dream_vacation = input("Where is your dream vacation? ")

    dream_vacations[user] = dream_vacation

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        responding = False

print("\n--- Poll Results ---")
for name, vacation in dream_vacations.items():
    print(name.title() + " would like to go to " + vacation.title() + ".")
