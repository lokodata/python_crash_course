from city_functions import city


def test_city_country():
    formatted_city = city('santiago', 'chile')
    assert formatted_city == 'Santiago, Chile'


def test_city_country_population():
    formatted_city = city('santiago', 'chile', 5000000)
    assert formatted_city == 'Santiago, Chile - population 5000000'
