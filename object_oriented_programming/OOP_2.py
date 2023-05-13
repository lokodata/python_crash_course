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


class icecreamstand(restaurant):
    def __init__(self, name, cuisine):
        super().__init__(name, cuisine)
        self.flavors = ['vanilla', 'chocolate',
                        'strawberry', 'mint', 'caramel']

    def display_flavors(self):
        print(f"{self.name} has the following flavors:")
        for flavor in self.flavors:
            print(f"{flavor.title()}")


icecreamstand_1 = icecreamstand('Baskin Robbins', 'Ice Cream')
icecreamstand_1.display_flavors()

print()


class user:
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.location = location.title()
        self.login_attempts = 0


class admin(user):
    def __init__(self, first_name, last_name, age, location):
        super().__init__(first_name, last_name, age, location)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def display_privileges(self):
        print(f"{self.first_name} {self.last_name} has the following privileges:")
        for privilege in self.privileges:
            print(f"{privilege.title()}")


admin_1 = admin('loko', 'data', 25, 'usa')
admin_1.display_privileges()

print()


class car:
    def __init__(self, make, model, year):
        self.make = make.title()
        self.model = model.title()
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You cannot roll back the odometer.')

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class battery:
    def __init__(self, battery_size=65):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 65:
            range = 260
        elif self.battery_size == 75:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size <= 65:
            self.battery_size = 75
            print('The battery has been upgraded.')
        else:
            print('The battery is already upgraded.')


class electric_car(car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = battery()


ec_car1 = electric_car('tesla', 'model s', 2019)
ec_car1.battery.describe_battery()
ec_car1.battery.get_range()
ec_car1.battery.upgrade_battery()
ec_car1.battery.get_range()
