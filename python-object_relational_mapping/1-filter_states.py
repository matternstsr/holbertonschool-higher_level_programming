#!/usr/bin/python3
"""SelectStates module
Write a script that lists all states from the database hbtn_0e_0_usa
Your script should take 3 arguments: mysql username, mysql password and
database name (no argument validation needed)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at
port 3306
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below
Your code should not be executed when imported"""

import MySQLdb
import sys


def select_states():
    """Grabs states from database"""

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    database = sys.argv[4]

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
