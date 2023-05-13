def city_country(city, country):
    return city.title() + ", " + country.title()


print(city_country('new york', 'united states'))
print(city_country('london', 'england'))
print(city_country('paris', 'france'))

print()


def make_album(artist_name, album_title, number_of_tracks=None):
    music_album = {'artist_name': artist_name, 'album_title': album_title}
    if number_of_tracks:
        music_album['number_of_tracks'] = number_of_tracks

    return music_album


print(make_album('eminem', 'recovery'))
print(make_album('eminem', 'recovery', 17))

print()

while True:
    still_creating = input("Still making an album? (y/n): ")
    if still_creating == 'n':
        break
    artist_name = input("Enter the artist name: ")
    album_title = input("Enter the album title: ")
    number_of_tracks = input("Enter the number of tracks: ")

    print(make_album(artist_name, album_title, number_of_tracks))
