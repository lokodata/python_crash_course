class restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def restaurant_served(self):
        print(f"{self.name} has served {self.number_served} customers.")

    def set_number_served(self, number_served):
        if number_served >= self.number_served:
            self.number_served = number_served
        else:
            print('You cannot roll back the number of customers served.')

    def increment_number_served(self, increment):
        self.number_served += increment


restaurant_1 = restaurant('McDonalds', 'American')

restaurant_1.restaurant_served()
restaurant_1.number_served = 10
restaurant_1.restaurant_served()

print()

restaurant_1.set_number_served(20)
restaurant_1.restaurant_served()

print()

restaurant_1.increment_number_served(30)
restaurant_1.restaurant_served()

print()


class user:
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.location = location.title()
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
        print('Login attempts reset.')


user_1 = user('loko', 'data', 25, 'usa')

user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()

print(f'User attempted to login {user_1.login_attempts} times')

user_1.reset_login_attempts()

print(f'User attempted to login {user_1.login_attempts} times')
