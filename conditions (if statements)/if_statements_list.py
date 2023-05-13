usernames = ['admin', 'joe', 'jane', 'john', 'jim']
for user in usernames:
    if user == 'admin':
        print("Hello " + user + ", would you like to see a status report?")
    else:
        print("Hello " + user + ", thank you for logging in again.")

print()

username1 = []

if username1 == []:
    print("We need to find some users!")

print()

current_users = ['admin', 'joe', 'jane', 'john', 'jim']
current_users_upper = [user.upper() for user in current_users]
new_users = ['admin', 'joe', 'jane', 'JOHN',
             'jim', 'joe1', 'jane1', 'john1', 'jim1']

for new_user in new_users:
    if new_user in current_users or new_user.upper() in current_users_upper:
        print("Please enter a new username.")
    else:
        print("This username is available.")

print()

numbers = list(range(1, 10))

for num in numbers:
    if num == 1:
        print(str(num) + "st")
    elif num == 2:
        print(str(num) + "nd")
    elif num == 3:
        print(str(num) + "rd")
    else:
        print(str(num) + "th")
