def make_shirt(size, message):
    print("The size of the shirt is " + size +
          " and the message is " + message + ".")


make_shirt('large', 'I love Python')
make_shirt(message='I love Python', size='large')

print()


def make_shirt(size='large', message='I love Python'):
    print("The size of the shirt is " + size +
          " and the message is " + message + ".")


make_shirt(size='medium')
make_shirt(message='I hate Python')

print()


def describe_city(city, country='United States'):
    print(city.title() + " is in " + country.title() + ".")


describe_city('new york')
describe_city('los angeles')
describe_city('london', 'england')
