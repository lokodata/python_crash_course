person = {'first_name': 'joe', 'last_name': 'smith',
          'age': 25, 'city': 'toronto'}

print(f'First name: {person["first_name"].title()} \nLast name: {person["last_name"].title()} \nAge: {person["age"]} \nCity: {person["city"].title()}')

print()

favorite_numbers = {'joe': 1, 'jane': 2, 'john': 3, 'jim': 4, 'joe1': 5}

print(f'Joe\'s favorite number is {favorite_numbers["joe"]}.')
print(f'Jane\'s favorite number is {favorite_numbers["jane"]}.')
print(f'John\'s favorite number is {favorite_numbers["john"]}.')
print(f'Jim\'s favorite number is {favorite_numbers["jim"]}.')
print(f'Joe1\'s favorite number is {favorite_numbers["joe1"]}.')

print()

glossary = {'list': 'a collection of items in a particular order', 'variable': 'a placeholder for a value', 'string': 'a series of characters',
            'comment': 'a note in a program that the Python interpreter ignores', 'loop': 'work through a collection of items, one at a time'}

print(f'List - {glossary["list"]}')
print(f'Variable - {glossary["variable"]}')
print(f'String - {glossary["string"]}')
print(f'Comment - {glossary["comment"]}')
print(f'Loop - {glossary["loop"]}')
print(f'Integer = {glossary.get("integer", "word not found.")}')
