import random


class die:
    def __init__(self, sides, rolls=0):
        self.sides = sides
        self.rolls = rolls

    def roll(self):
        print(f"Rolling a {self.sides}-sided die {self.rolls} times:")
        for i in range(self.rolls):
            print(f'\t{random.randint(1, self.sides)}')


die_1 = die(6, 10)
die_1.roll()

print()

die_2 = die(10, 10)
die_2.roll()

print()

die_3 = die(20, 10)
die_3.roll()

print()

num_let = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', "b", 'c', 'd', 'e']

lottery = random.choices(num_let, k=4)

print(f'Any ticket matching {lottery} wins a prize.')

print()

count = 0
lottery_1 = []

while lottery_1 != lottery:
    lottery_1 = random.choices(num_let, k=4)
    count += 1

print(f'After {count} tries, the winning ticket is {lottery_1}.')

print()
