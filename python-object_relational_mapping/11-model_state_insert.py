#!/usr/bin/python3
"""State module --  Write a script that adds the State object “Louisiana”
to the database hbtn_0e_6_usa
Your script should take 3 arguments: mysql username, mysql password and
database name.
You must use the module SQLAlchemy
You must import State and Base from model_state - from model_state import
Base, State.
Your script should connect to a MySQL server running on localhost at port 3306
Print the new states.id after creation
Your code should not be executed when imported"""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import State, Base


def create_a_state():
    """Fetching all states"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database,), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    new_state = State(name='Louisiana')
    session.add(new_state)

    state = session.query(State).filter_by(name='Louisiana').first()
    print("{}".format(state.id))
    session.close()


if __name__ == "__main__":
    create_a_state()
