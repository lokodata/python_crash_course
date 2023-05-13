city = ['Tokyo', 'New York', 'Toronto',
        'Hong Kong', 'Singapore', 'London', 'Shanghai']

middle = int(len(city)/2)

print(f'the first three items in the list are: \n{city[:3]}\n')
print(
    f'three items from the middle of the list are: \n{city[middle:middle+3]}\n')
print(f'the last three items in the list are: \n{city[-3:]}\n')

pizzas = ['pepperoni pizza', 'cheese pizza', 'veggie pizza']
friend_pizzas = pizzas[:]

pizzas.append('mushroom pizza')
friend_pizzas.append('pineapple pizza')

print(f'My favorite pizzas are: \n{pizzas}\n')
print(f'My friend\'s favorite pizzas are: \n{friend_pizzas}\n')

for pizza in pizzas:
    print(f'I like {pizza.title()}.')

print()

for pizza in friend_pizzas:
    print(f'My friend likes {pizza.title()}.')
