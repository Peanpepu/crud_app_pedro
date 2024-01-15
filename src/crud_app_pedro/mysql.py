from datetime import datetime

import pymysql


# MySQL connection parameters
username = "root"
password = "my-secret-pw"
hostname = "localhost"
port = 8001
database = "db"


_DB = None

def connect_to_database():
    """Create a singleton connection to a database

    The connection parameters for the database are taken from the enviroment.

    Additionally, it ensure the required tables are created on the DB.
    """
    global _DB
    if _DB is None:
        _DB = pymysql.connect(
            host=hostname,
            user=username,
            password=password,
            port=port,
            database=database,
            cursorclass=pymysql.cursors.DictCursor  # Use DictCursor for fetching results as dictionaries
        )

        ensure_table_exists()

def db_sync():
    """Commit the changes to the database
    """
    _DB.commit()

def table_exists(table_name: str, cursor) -> bool:
    """Checks whether a table exists through a existing cursor
    
    Args:
        table_name (str): Name of the table to check whether it exists.
        cursor (pymysql cursor): Cursor to execute queries on the database

    Returns:
        bool: Whether the table exists or not in the database.
    """
    query = f"SHOW TABLES LIKE '{table_name}'"
    cursor.execute(query)
    return cursor.fetchone() is not None

def ensure_table_exists():
    """Ensures all required tables exist in the associated database
    """
    with _DB.cursor() as cursor:
        if not table_exists("songs", cursor):
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS songs (
                    song_id INT PRIMARY KEY AUTO_INCREMENT,
                    song_name VARCHAR(255),
                    album VARCHAR(255), 
                    artist VARCHAR(255),
                    genre VARCHAR(255),
                    release_date TIMESTAMP NULL       
                )
                """
            )
        if not table_exists("users", cursor):
            # Ideally, it would have a password too
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    user_id INT PRIMARY KEY AUTO_INCREMENT,
                    user_name VARCHAR(255)      
                )
                """
            )

def add_song_to_db(song_name, album, artist, genre, release_date=None):
    with _DB.cursor() as cursor:
        insert_song_query = """
        INSERT INTO songs (song_name, album, artist, genre, release_date)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(insert_song_query, (song_name, album, artist, genre, release_date))

def search_song_by(song_name = None, artist = None):
    with _DB.cursor() as cursor:
        search_song_query = """
        SELECT * FROM songs
        WHERE (%s IS NULL OR song_name = %s)
        AND (%s IS NULL OR artist = %s)
        """
        cursor.execute(search_song_query, (song_name, song_name, artist, artist)) # This is ugly, must fix

        # Fetch all rows
        songs = cursor.fetchall()

        return songs

def user_exists(*, user_name: str = None, user_id: int = None):
    with _DB.cursor() as cursor:
        query = f"""select user_id from users where
        (%s IS NOT NULL AND user_name = %s)
        OR (%s IS NOT NULL AND user_id = %s)""" # and password = "%s"
        cursor.execute(query, (user_name, user_name, user_id, user_id)) # This is ugly, must fix
        return cursor.fetchone()
    
def create_user(user: str):
    with _DB.cursor() as cursor:
        insert_song_query = """
        INSERT INTO users (user_name)
        VALUES (%s)
        """
        cursor.execute(insert_song_query, (user,))

#connect_to_database()
#create_user("pepe")
#db_sync()