for i in range(1, 21):
    print(i)

print()

one_million = list(range(1, 1000001))
# print(one_million)

print(min(one_million))
print(max(one_million))
print(sum(one_million))

print()

odd_numbers = list(range(1, 21, 2))
for odd in odd_numbers:
    print(odd)

print()

threes = [num for num in range(0, 31) if num % 3 == 0]
print(threes)

print()

cubes = []
for num in range(1, 11):
    cubes.append(num**3)
print(cubes)

cubes = [num**3 for num in range(1, 11)]
print(cubes)
