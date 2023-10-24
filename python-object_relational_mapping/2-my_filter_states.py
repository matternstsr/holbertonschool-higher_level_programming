#!/usr/bin/python3
"""
SelectStates module - Write a script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa where name matches
the argument.
Your script should take 4 arguments: mysql username, mysql password,
database name and state name searched (no argument validation needed)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
You must use format to create the SQL query with the user input
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below
Your code should not be executed when imported
"""

import sys


def find_state():
    """Finds states with the given name in database"""

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    searched = sys.argv[4]

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database)
    database_cursor = db.cursor()
    database_cursor.execute("""SELECT *\
                FROM states\
                WHERE name LIKE BINARY '{}'\
                ORDER BY id ASC""".format(searched))
    rows = database_cursor.fetchall()
    for row in rows:
        print(row)
    database_cursor.close()
    db.close()


if __name__ == "__main__":
    find_state()
