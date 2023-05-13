from OOP_3_1 import restaurant
from OOP_3_1 import admin
import OOP_3_2

restaurant_1 = restaurant('McDonalds', 'American')
restaurant_1.number_served = 5
restaurant_1.describe_restaurant()

print()

user_1 = admin('loko', 'data', 25, 'usa')
user_1.display_privileges()

print()

admin_1 = OOP_3_2.admin('loko', 'data', 25, 'usa')
admin_1.display_privileges()
