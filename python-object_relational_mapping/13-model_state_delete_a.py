#!/usr/bin/python3
"""State module --  Write a script that deletes all State objects
with a name containing the letter a from the database hbtn_0e_6_usa
Your script should take 3 arguments: mysql username, mysql password
and database name
You must use the module SQLAlchemy
You must import State and Base from model_state - from model_state
import Base, State
Your script should connect to a MySQL server running on localhost
at port 3306
Your code should not be executed when imported"""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import State, Base


def update_state():
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

    for state in session.query(State).filter(
            State.name.like('%a%')):
        session.delete(state)

    session.commit()
    session.close()


if __name__ == "__main__":
    update_state()
