class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        self.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artist_count()

    def add_song_to_count(self):
        """Increment the total song count by 1."""
        Song.count += 1

    def add_to_genres(self):
        """Add this song's genre to the class genres list if not already present."""
        if self.genre not in Song.genres:
            Song.genres.append(self.genre)

    def add_to_artists(self):
        """Add this song's artist to the class artists list if not already present."""
        if self.artist not in Song.artists:
            Song.artists.append(self.artist)

    def add_to_genre_count(self):
        """Increment this genre's count, or set it to 1 if it doesn't exist yet."""
        if self.genre in Song.genre_count:
            Song.genre_count[self.genre] += 1
        else:
            Song.genre_count[self.genre] = 1

    def add_to_artist_count(self):
        """Increment this artist's count, or set it to 1 if it doesn't exist yet."""
        if self.artist in Song.artist_count:
            Song.artist_count[self.artist] += 1
        else:
            Song.artist_count[self.artist] = 1