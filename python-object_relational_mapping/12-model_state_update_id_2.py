#!/usr/bin/python3
"""State module --  Write a script that changes the name of a State
object from the database hbtn_0e_6_usa
Your script should take 3 arguments: mysql username, mysql password
and database name
You must use the module SQLAlchemy
You must import State and Base from model_state - from model_state
import Base, State
Your script should connect to a MySQL server running on localhost
at port 3306
Change the name of the State where id = 2 to New Mexico
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

    state_to_update = session.query(State).filter_by(id=2).first()

    if state_to_update:
        # Update the state's name
        state_to_update.name = "New Mexico"
        session.commit()
        print("State with id 2 has been updated to 'New Mexico'")

    session.close()


if __name__ == "__main__":
    create_a_state()
