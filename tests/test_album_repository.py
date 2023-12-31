from lib.album_repository import *
from lib.album import *

def test_get_all_records(db_connection):
    db_connection.seed("seeds/music_library.sql") # Seed our database with some test data
    repository = AlbumRepository(db_connection) # Create a new ArtistRepository

    albums = repository.all()

    assert albums == [
        Album(1,'Doolittle', 1989, 1),
        Album(2, 'Surfer Rosa', 1988, 1),
        Album(3, 'Waterloo', 1974, 2),
        Album(4, 'Super Trouper', 1980, 2),
        Album(5, 'Bossanova', 1990, 1),
        Album(6, 'Lover', 2019, 3),
        Album(7, 'Folklore', 2020, 3),
        Album(8, 'I Put a Spell on You', 1965, 4),
        Album(9, 'Baltimore', 1978, 4),
        Album(10, 'Here Comes the Sun', 1971, 4),
        Album(11, 'Fodder on My Wings', 1982, 4),
        Album(12, 'Ring Ring', 1973, 2)
    ]

"""
Find method gets one album
Arg = id
SQL = SELECT * FROM albums WHERE id = $1;
Returns = single album
"""

def test_find_single_album(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    albums = repository.find(1)
    assert albums == Album(1,'Doolittle', 1989, 1)


"""
def test_create_adds_album_to_albums()
repository.create('New album', 2023, 1)
albums = repository.all()
assert albums[-1] == Album('New album', 2023, 1)
"""

def test_create_adds_album_to_albums(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    repository.create('New album', 2023, 1)
    albums = repository.all()
    assert albums[-1] == Album(13, 'New album', 2023, 1)


"""
def test_delete_adds_album_to_albums()
repository.delete(12)
albums = repository.all()
assert albums[-1] == Album(11, 'Fodder on My Wings', 1982, 4)
"""

def test_delete_adds_album_to_albums(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    repository.delete(12)
    albums = repository.all()
    assert albums[-1] == Album(11, 'Fodder on My Wings', 1982, 4)