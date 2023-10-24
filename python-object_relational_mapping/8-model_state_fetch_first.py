#!/usr/bin/python3
"""State module --  Write a script that prints the first State object
from the database hbtn_0e_6_usa.
Your script should take 3 arguments: mysql username, mysql password and
database name. You must use the module SQLAlchemy
You must import State and Base from model_state - from model_state import
Base, State. Your script should connect to a MySQL server running on localhost at port 3306
The state you display must be the first in states.id
You are not allowed to fetch all states from the database before 
displaying the result. The results must be displayed as they are in the example below
If the table states is empty, print Nothing followed by a new line
Your code should not be executed when imported"""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State


def fetch_first():
    """Fetchs all states"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    state = session.query(State).first()
    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")
    session.close()

if __name__ == "__main__":
    fetch_first()
