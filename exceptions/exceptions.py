from pathlib import Path

try:
    num_1 = int(input("Enter a number: "))
    num_2 = int(input("Enter another number: "))
except ValueError:
    print('You must enter a number.')
else:
    print(f'{num_1} + {num_2} = {num_1 + num_2}')

print()

while True:
    try:
        num_1 = int(input("Enter a number: "))
        num_2 = int(input("Enter another number: "))
    except ValueError:
        print('You must enter a number.')
    else:
        print(f'{num_1} + {num_2} = {num_1 + num_2}')
        break

print()

try:
    path = Path('cats.txt')
    path2 = Path('dogs.txt')
    print(path.read_text())
    print(path2.read_text())
except FileNotFoundError:
    print('File not found.')

print()

try:
    path = Path('cats.txt')
    path2 = Path('dogs.txt')
    print(path.read_text())
    print(path2.read_text())
except FileNotFoundError:
    pass

print()

path_1 = Path('the_blue_castle.txt')
contents = path_1.read_text(encoding='utf-8')
words = contents.split()
num_words = len(words)
print(f'The Blue Castle has {num_words} words.')
print(words.count('the'))
print(words.count('the '))
