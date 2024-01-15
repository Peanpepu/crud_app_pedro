# Sample CRUD app

## Domain
This example is going to be made on Music.

Sample attributes used for the DB:
- Song name: str
- Album: str
- Artist: str
- Genre: str
- Release date: datetime

Some of this may be moved to new tables to add more information (for example, extra data on the artists) but for this example we will use a single table design.

## Requisites
* Must have a Command Line Interface (CLI) with argparse (alternatives: fire, click, typer)
* Must use a MySQL for persistance and querying the data (alternatives: PostgreSQL, Oracle, MongoDB, Cassandra, ...)
    * Optional the use of an ORM like SQLalchemy.
    * If not using a ORM, must use Pandas as the internal table/row format
* Must allow to do CRUD operations from the CLI.
* Test at least the main logic of the application
* Make sure to write quality maintainable code, we may use it in the future. Use abstractions when neccesary (can I easily change the DB in the future?), document the code, use typing, ...
    * Write a README file with all relevant information on using and testing the app
    * Optional: Upload your code to Github
### Extensions
* Authenticate the user. Un-authenticated users can only query the data. Authenticated users can add, edit or delete them.
* Allow to export/import the full database to at least two standard formats: CSV, JSON, ...
* Dockerize the application