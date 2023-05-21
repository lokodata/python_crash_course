def city(city_name, country_name, population=None):
    city = f"{city_name.title()}, {country_name.title()}"
    if population:
        return f"{city_name.title()}, {country_name.title()} - population {population}"
    return city
