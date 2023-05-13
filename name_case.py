name = 'John'

message = f"Hello, {name.title()}! Would you like to learn some Python today?"

name_title = name.title()
name_upper = name.upper()
name_lower = name.lower()

print(message)

print()

print(f'{name} in title format, {name_title}')
print(f'{name} in upper format, {name_upper}')
print(f'{name} in lower format, {name_lower}')

print()

print('''Albert Einstein once said, "A person who never made a mistake never tried anything new."''')

print()

famous_person = 'Albert Einstein'
message = '"I live in the present due to the fact that I am always learning new things."'

print(f'{famous_person} once said, {message}')

print()

name = '\tJohn\n'

print(name.rstrip())
print(name.lstrip())
print(name.strip())

print()

filename = 'python_notes.txt'

print(filename.removesuffix('.txt'))
