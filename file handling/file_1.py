from pathlib import Path

name = input("Enter your name: ")

path = Path('guest.txt')
path.write_text(name)

print(path.read_text())

print()

names = ''

while True:
    name = input("Enter your name: ")
    if name == 'q':
        break
    else:
        names += name + '\n'

path = Path('guest_book.txt')
path.write_text(names)

print(path.read_text())
