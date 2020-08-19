import sqlite3
from sqlite3 import Error
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(message)s"
)

# This file provides a general interface to complete database
# operations. It could be used for any project.

# Create a database connection
# :param db_filepath: database file path
# :return: Connection object or None
def create_connection(db_filepath):
    conn = None
    try:
        conn = sqlite3.connect(db_filepath)

        # Completion Output (for testing)
        # print(sqlite3.version)
    except Error as e:
        print(e)

    return conn

# Execute a statement
# :param conn: Connection Object
# :param command: An SQL statement to run
def execute(conn, command):
    try:
        cur = conn.cursor()
        cur.execute(command)
    except Error as e:
        print(e)
    return cur

# Execute a statement with variables
# :param conn: Connection Object
# :param command: An SQL statement to run
# :param vars: a tuple to fill in the SQL statement vars
def execute_with_vars(conn, command, vars):
    try:
        cur = conn.cursor()
        cur.execute(command, vars)
    except Error as e:
        print(e)
    return cur