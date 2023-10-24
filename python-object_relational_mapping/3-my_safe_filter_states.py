#!/usr/bin/python3
"""
SelectStates module --  Wait, do you remember the previous task? 
Did you test "Arizona'; TRUNCATE TABLE states ; SELECT * FROM states
WHERE name = '" as an input?
What? Empty?
Yes, it’s an SQL injection to delete all records of a table…
Once again, write a script that takes in arguments and displays 
all values in the states table of hbtn_0e_0_usa where name matches 
the argument. But this time, write one that is safe from MySQL injections!
Your script should take 4 arguments: mysql username, mysql password, 
database name and state name searched (safe from MySQL injection)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below
Your code should not be executed when imported
"""
import MySQLdb
import sys


def safe_find_state():
    """Finds states with the given name in database"""

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    searched = sys.argv[4]

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database
                         )
    database_cursor = db.cursor()
    database_cursor.execute("SELECT *\
                FROM states\
                WHERE name = %(searched_name)s\
                ORDER BY id ASC",
                {'searched_name': searched}
                )
    rows = database_cursor.fetchall()
    for row in rows:
        print(row)
    database_cursor.close()
    db.close()


if __name__ == "__main__":
    safe_find_state()
