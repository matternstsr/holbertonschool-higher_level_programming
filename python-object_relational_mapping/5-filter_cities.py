#!/usr/bin/python3
""" Write a script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
Your script should take 4 arguments: mysql username, mysql password,
database name and state name (SQL injection free!)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by cities.id
You can use only execute() once
The results must be displayed as they are in the example below
Your code should not be executed when imported"""
import MySQLdb
import sys

if __name__ == "__main__":

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

    query = '''SELECT *
            FROM cities
            JOIN states ON cities.state_id = states.id
            ORDER BY cities.id ASC;
            '''
    database_cursor.execute(query)

    cities = database_cursor.fetchall()

    print_cities = [city[2] for city in cities if city[4] == sys.argv[4]]
    print(', '.join(print_cities))

    database_cursor.close()
    db.close()
