#!/usr/bin/python3
"""SelectStates module"""
import MySQLdb
import sys


def select_states():
    """Grabs states from the database"""

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database)
    database_cursor = db.cursor()
    database_cursor.execute('SELECT * FROM states ORDER BY id ASC')
    states = database_cursor.fetchall()
    for state in states:
        print(state)
    database_cursor.close()
    db.close()


if __name__ == "__main__":
    select_states()
