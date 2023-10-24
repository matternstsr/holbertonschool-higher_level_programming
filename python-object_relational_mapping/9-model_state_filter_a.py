#!/usr/bin/python3
"""State module --  Write a script that lists all State objects that contain
the letter a from the database hbtn_0e_6_usa
Your script should take 3 arguments: mysql username, mysql password and
database name. You must use the module SQLAlchemy
You must import State and Base from model_state - from model_state
import Base, State. Your script should connect to a MySQL server
running on localhost at port 3306. Results must be sorted in
ascending order by states.id
The results must be displayed as they are in the example below
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

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    for state in session.query(State).filter(
            State.name.like('%a%')).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
    session.close()


if __name__ == "__main__":
    fetch_all()
