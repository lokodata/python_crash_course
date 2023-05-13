from OOP_3_1 import user


class admin(user):
    def __init__(self, first_name, last_name, age, location):
        super().__init__(first_name, last_name, age, location)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def display_privileges(self):
        print(f"{self.first_name} {self.last_name} has the following privileges:")
        for privilege in self.privileges:
            print(f"{privilege.title()}")
