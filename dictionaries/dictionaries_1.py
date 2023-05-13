glossary = {'list': 'a collection of items in a particular order', 'variable': 'a placeholder for a value', 'string': 'a series of characters',
            'comment': 'a note in a program that the Python interpreter ignores', 'loop': 'work through a collection of items, one at a time', 'integer': 'a whole number',
            'float': 'any number with a decimal point', 'boolean': 'a true or false value', 'dictionary': 'a collection of key-value pairs', 'key': 'the first item in a key-value pair'}

for key, value in glossary.items():
    print(f'{key.title()} - {value}')

print()

rivers = {'nile': 'egypt', 'amazon': 'brazil', 'yangtze': 'china'}

for key, value in rivers.items():
    print(f'The {key.title()} runs through {value.title()}.')
    print(f'{key.title()}')
    print(f'{value.title()}')

print()

favorite_languages = {'jen': 'python', 'sarah': 'c',
                      'edward': 'ruby', 'phil': 'python', 'lenny': '', 'joe': 'c++'}

for key, value in favorite_languages.items():
    if value == '':
        print(f'{key.title()}, please take our poll!')
    else:
        print(f'{key.title()}, thank you for taking the poll!')
