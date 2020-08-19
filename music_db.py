import os
import db
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(message)s"
)

# Get the working directory and initialize the database
cur_dir = Path(os.path.dirname(os.path.realpath(__file__)))
db_filepath = (cur_dir / "music.db").__str__()

# This is a simple database with two tables; a song table, and a content table.
# The content table references the song it's related to. The song table does not
# reference the content table directly.

# Table 1:
## Create Table 'songs'
### Song ID:      int
### Song Name:    str
### Artist:       str
sql_create_song_table =     """ CREATE TABLE IF NOT EXISTS songs (
                                id integer PRIMARY KEY,
                                song_name text NOT NULL,
                                artist_name text NOT NULL
                            ); """
## Insert into table songs
sql_insert_song = '''   INSERT INTO songs(song_name,artist_name)
                        VALUES(?,?) '''
## Select into table songs
sql_select_song = '''   SELECT * FROM songs WHERE song_name=? '''
sql_select_song_by_artist = '''   SELECT * FROM songs WHERE song_name=? AND artist_name=?'''

# Table 2:
## Create Table 'content'
### Content ID:   int
### Content:      str (filepath or link)
### Song ID:      int 
sql_create_content_table = """  CREATE TABLE IF NOT EXISTS content (
                                id integer PRIMARY KEY,
                                content_path text NOT NULL,
                                song_id integer NOT NULL,
                                FOREIGN KEY (song_id) REFERENCES songs (id)
                            ); """
sql_insert_content = '''   INSERT INTO content(content_path,song_id)
                        VALUES(?,?) '''
sql_select_content = '''   SELECT * FROM content WHERE content_path=? AND song_id=?'''

# A song name should be provided for access to any particular record
# The other options are optional unless multiple songs have the same name.

# Initialize the DB with the required structure
# If it exists, check for correct structure
def initialize_DB(db_filepath):
    conn = None
    logging.debug("Initializing database.")

    # Establish connection
    conn = db.create_connection(db_filepath)
    if conn:
        logging.debug("Database initialized.")
    else:
        print("FAILED")

    if conn is None:
        return conn

    # Create Tables if DNE
    db.execute(conn, sql_create_song_table)
    db.execute(conn, sql_create_content_table)

    return conn

# Add a record to the database
def add_record(song, artist=None, content=None):
    conn = initialize_DB(db_filepath)
    with conn:
        # Get correct query
        if (artist):
            song_record = [song, artist]
            sql_select_song_general = sql_select_song_by_artist
        else:
            song_record = [song]
            sql_select_song_general = sql_select_song

        # Check if song already exists
        cur = db.execute_with_vars(conn, sql_select_song_general, song_record)
        record = cur.fetchone()

        # If record does not exist, add the song
        if (record is None):
            cur = db.execute_with_vars(conn, sql_insert_song, song_record)

        # Obtain the song_id from newly added song
        cur = db.execute_with_vars(conn, sql_select_song_general, song_record)
        record = cur.fetchone()

        # Record is in format (id, song_name, artist_name)
        song_id = record[0]

        # If content exists, add the content
        if (content is not None):
            # Add content links using song_id
            content_record = [content, song_id]
            cur = db.execute_with_vars(conn, sql_select_content,content_record)

            if cur.fetchone() is None:
                cur = db.execute_with_vars(conn, sql_insert_content, content_record)
    # Create song
    logging.info("Adding a record")

# Edit a record in the database
def edit_record(oldSong, oldArtist=None, oldContent=None, newSong=None, newArtist=None, newContent=None):
    logging.info("Editing a record")

# Delete a record in the database
def delete_record(song, artist=None, content=None):
    logging.info("Deleting a record")

# Display records with various search criteria.
# Find a particular song, list the songs by an artist,  or both.
def display_record(song=None, artist=None):
    logging.info("Displaying a record") 

# Return the links and filepaths related to a particular song
def return_records(song=None, artist=None):
    logging.info("Opening links of record") 