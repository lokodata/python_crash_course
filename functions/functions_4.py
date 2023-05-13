def sandwich(*ingredients):
    print("The sandwich will have the following ingredients:")
    for ingredient in ingredients:
        print("- " + ingredient)


sandwich('ham', 'cheese', 'lettuce')
sandwich('turkey')
sandwich('peanut butter', 'jelly')

print()


def build_profile(first_name, last_name,  **user_info):
    user_info['first_name'] = first_name
    user_info['last_name'] = last_name
    return user_info


print(build_profile('loko', 'data', location='USA', field='computer science'))

print()


def cars(manufacturer, model, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info


print(cars('subaru', 'outback', color='blue', tow_package=True))
