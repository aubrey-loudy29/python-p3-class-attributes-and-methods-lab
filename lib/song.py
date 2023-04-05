class Song:
    count = 0
    artists = []
    artist_count = {}
    genres = []
    genre_count = {}

    def __init__(self, name, artist, genre) :
        self.add_song_to_count()
        self.add_to_artists(artist)
        self.add_to_genres(genre)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)

        self.name = name
        self.artist = artist
        self.genre = genre

    @classmethod 
    def add_song_to_count(the_class, increment = 1) :
        the_class.count += increment

    @classmethod
    def add_to_artists(the_class, artist) :
        the_class.artists.append(artist)

    @classmethod
    def add_to_genres(the_class, genre) :
        the_class.genres.append(genre)

    @classmethod 
    def add_to_artist_count(the_class, artist) :
        if artist in the_class.artist_count :
            the_class.artist_count[artist] += 1
        else: 
            the_class.artist_count[artist] = 1

    @classmethod 
    def add_to_genre_count(the_class, genre) :
        if genre in the_class.genre_count :
            the_class.genre_count[genre] += 1
        else: 
            the_class.genre_count[genre] = 1
