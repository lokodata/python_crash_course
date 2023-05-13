car = 'subaru'
car2 = 'toyota'
num = 1
num2 = 5
list = [1, 2, 3, 4, 5]

print(f'Is car == "subaru"? I predict True. \nAnswer is {car == "subaru"}\n')
print(f'Is car2 == "toyota"? I predict True. \nAnswer is {car2 == "toyota"}\n')
print(f'Is car == car2? I predict False. \nAnswer is {car == car2}\n')
print(
    f'Is car == car.upper? I predict False. \nAnswer is {car == car.upper()}\n')
print(
    f'Is car2 == car2.lower? I predict False. \nAnswer is {car2 == car2.lower()}\n')
print(f'Is num == 1? I predict True. \nAnswer is {num == 1}\n')
print(f'Is num2 != 1? I predict True. \nAnswer is {num2 != 1}\n')
print(f'Is num > 0? I predict True. \nAnswer is {num > 0}\n')
print(f'Is num2 < 0? I predict False. \nAnswer is {num2 < 0}\n')
print(f'Is num in list? I predict True. \nAnswer is {num in list}\n')
print(f'Is num2 not in list? I predict True. \nAnswer is {num2 not in list}\n')
print(
    f'Is num and num2 in list? I predict True. \nAnswer is {num and num2 in list}\n')
print(f'Is 8 or 1 in list? I predict True. \nAnswer is {8 or 1 in list}\n')
