import argparse
import os

import load_dotenv

from crud_app_pedro.auth import is_logged_in, login, logout
from crud_app_pedro.db import DataBase
from crud_app_pedro.db_mongo import MongoDataBase


def main():
    # Use argparser to create the CLI for the application
    # It uses a subparser to separate the 4 parts of CRUD
    parser = argparse.ArgumentParser(description="CRUD operations over a music DB")
    # Alternatively, you can add here global parameters for login the user
    subparsers = parser.add_subparsers(help="Subcommands", dest="command")

    # Subparser for the 'login' command
    login_parser = subparsers.add_parser("login", help="Login to the DB")
    login_parser.add_argument("--user", help="User to autheticate as", required=True)
    # A password should probably be provided

    # Subparser for the 'logout' command
    logout_parser = subparsers.add_parser("logout", help="Logout of the DB")

    # Subparser for the 'create' command
    create_parser = subparsers.add_parser("create", help="Add a song to the DB")
    create_parser.add_argument("--song", help="Name of the song", required=True)
    create_parser.add_argument("--album", help="Name of the album", required=True)
    create_parser.add_argument("--artist", help="Name of the artist", required=True)
    create_parser.add_argument("--genre", help="Name of the genre", required=True)
    create_parser.add_argument(
        "--release_date", help="Release date of the song", default=None, required=False
    )

    # Subparser for the 'search' command
    search_parser = subparsers.add_parser("search", help="Search in the music db")
    search_parser.add_argument("--song", help="Name of the song", default=None)
    search_parser.add_argument("--artist", help="Name of the artist", default=None)

    # Parse the args
    args = parser.parse_args()

    # Ensure we are connected to the database
    load_dotenv.load_dotenv()
    connection_str = os.getenv("CRUD_APP_CONNECTION_STR")

    if connection_str is None:
        print(
            "Provide the mongoDB connection string via the environment variable CRUD_APP_CONNECTION_STR"
        )
        exit(-1)

    db: DataBase = MongoDataBase(connection_str)

    match args.command:
        case "login":
            login(user=args.user, db=db)
        case "logout":
            logout()
        case "create":
            if not is_logged_in(db=db):
                print("Please login using the login subcommand")
                exit()
            db.add_song(
                args.song, args.album, args.artist, args.genre, args.release_date
            )
            print("Success! Song inserted into DB")
        case "search":
            print(db.search_song_by(args.song, args.artist))
        case _:
            parser.print_help()

    # Sync any possible changes with the database
    db.sync()


if __name__ == "__main__":
    main()
