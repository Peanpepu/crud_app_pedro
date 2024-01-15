from pymongo import MongoClient

from db import DataBase


class MongoDataBase(DataBase):
    def __init__(self, mongo_connection_str: str):
        self._client = MongoClient(mongo_connection_str)
        self._db = self._client["master-crup-apps"]
        self._songs = self._db["songs"]
        self._auth = self._db["auth"]

    def add_song(
        self, song: str, album: str, artist: str, genre: str, release_date: str
    ):
        self._songs.insert_one(
            {
                "song": song,
                "album": album,
                "artist": artist,
                "genre": genre,
                "release_date": release_date,
            }
        )

    def search_song_by(self, song: str, artist: str):
        pass

    def sync(self):
        pass

    def user_exists(self, user: str):
        pass
