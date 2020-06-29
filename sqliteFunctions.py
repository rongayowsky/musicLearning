import sqlite3

# This is a simple database with two tables; a song table, and a content table.
# The content table references the song it's related to. The song table does not
# reference the content table directly.

# Table 1:
# Song ID:      int
# Song Name:    str
# Artist:       str

# Table 2:
# Content ID:   int
# Content:      str (filepath or link)
# Song ID:      int 

# A song name should be provided for access to any particular record
# The other options are optional unless multiple songs have the same name.

# Initialize the DB with the required structure
# If it exists, check for correct structure
def initialize_DB():
    print("Initializing DB")

# Add a record to the database
def add_record(song, artist=None, content=None):
    print("Adding a record")

# Edit a record in the database
def edit_record(oldSong, oldArtist=None, oldContent=None, newSong=None, newArtist=None, newContent=None):
    print("Editing a record")

# Delete a record in the database
def delete_record(song, artist=None, content=None):
    print("Deleting a record")

# Display records with various search criteria.
# Find a particular song, list the songs by an artist,  or both.
def display_record(song=None, artist=None):
    print("Displaying a record") 

# Return the links and filepaths related to a particular song
def return_records(song=None, artist=None):
    print("Opening links of record") 