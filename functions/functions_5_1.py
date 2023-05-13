def sandwich(*ingredients):
    print("The sandwich will have the following ingredients:")
    for ingredient in ingredients:
        print("- " + ingredient)


def build_profile(first_name, last_name,  **user_info):
    user_info['first_name'] = first_name
    user_info['last_name'] = last_name
    return print(user_info)


def cars(manufacturer, model, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return print(car_info)
