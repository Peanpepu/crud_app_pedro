from abc import ABC, abstractmethod

class DataBase(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def user_exists(self, user: str):
        pass

    @abstractmethod
    def add_song(self, song: str, album: str, artist: str, genre: str, release_date: str):
        pass

    @abstractmethod
    def search_song_by(self, song: str, artist: str):
        pass

    @abstractmethod
    def sync(self):
        pass
