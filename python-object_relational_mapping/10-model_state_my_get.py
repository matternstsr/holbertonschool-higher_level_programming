#!/usr/bin/python3
"""State module --  Write a script that prints the State object with
the name passed as argument from the database hbtn_0e_6_usa
Your script should take 4 arguments: mysql username, mysql password,
database name and state name to search (SQL injection free)
You must use the module SQLAlchemy
You must import State and Base from model_state - from model_state
import Base, State
Your script should connect to a MySQL server running on localhost
at port 3306
You can assume you have one record with the state name to search
Results must display the states.id
If no state has the name you searched for, display Not found
Your code should not be executed when imported"""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State


def fetch_all():
    """Fetching all states"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    statenametosearch = sys.argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database, statenametosearch), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    for state in session.query(State).filter(
            State.name.like('%a%')).order_by(State.id):
        if state:
            print("{}: {}".format(state.id, state.name))
        else:print("Not found")
    session.close()


if __name__ == "__main__":
    fetch_all()
