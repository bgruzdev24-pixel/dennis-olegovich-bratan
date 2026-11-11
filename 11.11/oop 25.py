class Playlist:
    def __init__(self):
        self._songs = []

    def add_song(self, song):
        self._songs.append(song)

    def remove_song(self, song):
        self._songs.remove(song)

    @property
    def songs(self):
        return tuple(self._songs)


playlist = Playlist()
playlist.add_song("Море")
playlist.add_song("In the End")
print(playlist.songs)  

playlist.remove_song("Море")
print(playlist.songs)  