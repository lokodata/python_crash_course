people = [{'name': 'Mary', 'height': 160}, {
    'name': 'Isla', 'height': 80}, {'name': 'Sam', 'height': 180}]

for person in people:
    for info in person:
        print(f'{info.title()} - {person[info]}')
    print()

pets = [{'name': 'fido', 'animal': 'dog', 'owner': 'john'},
        {'name': 'mittens', 'animal': 'cat', 'owner': 'jane'},
        {'name': 'rover', 'animal': 'dog', 'owner': 'joe'},
        {'name': 'fluffy', 'animal': 'cat', 'owner': 'jim'}]

for pet in pets:
    for info in pet:
        print(f'{info.title()} - {pet[info].title()}')
    print()

favorite_places = {'joe': ['toronto', 'new york', 'london'],
                   'jane': ['paris', 'rome', 'tokyo'],
                   'john': ['sydney', 'tokyo', 'london']}

for name, places in favorite_places.items():
    print(f'{name.title()}\'s favorite places are:')
    for place in places:
        print(place.title())
    print()


favorite_numbers = {'joe': [1, 2, 3], 'jane': [4, 5, 6], 'john': [7, 8, 9]}

for name, number in favorite_numbers.items():
    print(f'{name.title()}\'s favorite numbers are:')
    for num in number:
        print(num)
    print()

cities = {'toronto': {'country': 'canada', 'population': 1000000}, 'new york': {'country': 'united states', 'population': 2000000},
          'london': {'country': 'united kingdom', 'population': 3000000}}

for city, info in cities.items():
    print(
        f'{city.title()} is in {info["country"].title()} and has a population of {info["population"]}.')
