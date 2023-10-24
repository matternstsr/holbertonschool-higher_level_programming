#!/usr/bin/python3
"""
SelectStates module -- Write a script that lists all cities from the
database hbtn_0e_4_usa
Your script should take 3 arguments: mysql username, mysql password
and database name
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by cities.id
You can use only execute() once
Results must be displayed as they are in the example below
Your code should not be executed when imported
"""
import MySQLdb
import sys


def select_cities():
    """Selects all cities in database"""

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database
                         )
    database_cursor = db.cursor()
    database_cursor.execute("SELECT cities.id, cities.name, states.name\
                FROM cities\
                INNER JOIN states\
                ON cities.state_id = states.id\
                ORDER BY cities.id ASC")
    rows = database_cursor.fetchall()
    for row in rows:
        print(row)
    database_cursor.close()
    db.close()


if __name__ == "__main__":
    select_cities()
