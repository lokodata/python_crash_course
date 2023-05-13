class restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        print(f"{self.name} serves {self.cuisine} cuisine.")

    def open_restaurant(self):
        print(f"{self.name} is open for business!")


restaurant_1 = restaurant('McDonalds', 'American')
restaurant_2 = restaurant('Taco Bell', 'Mexican')
restaurant_3 = restaurant('Panda Express', 'Chinese')

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()

restaurant_1.open_restaurant()

print()


class user:
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.location = location.title()

    def describe_user(self):
        print(
            f"{self.first_name} {self.last_name} is {self.age} years old and lives in {self.location}.")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}!")


user_1 = user('loko', 'data', 25, 'usa')
user_2 = user('john', 'doe', 30, 'canada')
user_3 = user('jane', 'doe', 28, 'mexico')

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()

user_3.describe_user()
user_3.greet_user()
