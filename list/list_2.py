places = ["New Zealand", "Tokyo", "Iceland", "New York", "Maldives"]

print(places)

print()

print(sorted(places))
print(places)

print()

places.reverse()
print(places)

places.reverse()
print(places)

print()

places.sort()
print(places)

places.sort(reverse=True)
print(places)
print(len(places))

print()

mountains = ["Mount Everest", "K2", "Kangchenjunga", "Lhotse", "Makalu"]

print(
    f'I want to visit the mountains of {mountains[0]}, {mountains[1]}, {mountains[2]}, {mountains[3]}, and {mountains[4]}')

mountains.append("Cho Oyu")
print(mountains)

print()

mountains[0] = "Everest"
print(mountains)

print()

mountains.insert(0, "Dhaulagiri")
mountains.insert(3, "Manaslu")
print(mountains)

print()

popped_item = mountains.pop(1)
print(f'Item popped: {popped_item}')
print(mountains)

print()

mountains.remove('K2')
print(mountains)

print()

del mountains[0]
print(mountains)

print()

print(sorted(mountains))
print(mountains)

print()

mountains.sort()
print(mountains)

print()

mountains.reverse()
print(mountains)

print(len(mountains))
