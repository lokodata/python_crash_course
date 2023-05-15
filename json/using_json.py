from pathlib import Path
import json

favorite_number = input('Enter your favorite number: ')

path = Path('fav_number.json')
contents = json.dumps(favorite_number)
path.write_text(contents)

contents1 = path.read_text()
number = json.loads(contents1)
print(f'I know your favorite number! It’s {number}.')

print()

favorite_number = input('Enter your favorite number: ')

path = Path('fav_number.json')
contents1 = path.read_text()
number = json.loads(contents1)

if favorite_number == number:
    print(f'I know your favorite number! It’s {number}.')
else:
    contents = json.dumps(favorite_number)
    path.write_text(contents)
    print(f'I’ll remember that your favorite number is {favorite_number}.')

print()


def get_stored_user(path):
    if path.exists():
        contents1 = path.read_text()
        return json.loads(contents1)
    else:
        return None


def get_new_user(path):
    username = input('What is your name? ')
    age = input('How old are you? ')
    favorite_number = input('Enter your favorite number: ')
    dict = {'username': username, 'age': age,
            'favorite_number': favorite_number}
    contents = json.dumps(dict)
    path.write_text(contents)
    return dict


def greet_user():
    verify = input('Are you a returning user? (y/n) ')

    path = Path('user.json')
    user = get_stored_user(path)

    if verify == 'y' and user != None:
        print(f'Welcome back, {user["username"]}!')
        print(
            f'User: {user["username"]}!\nAge: {user["age"]}!\nFavorite number: {user["favorite_number"]}!')
    else:
        user = get_new_user(path)
        print(f'We\'ll remember you when you come back, {user["username"]}!')


greet_user()
