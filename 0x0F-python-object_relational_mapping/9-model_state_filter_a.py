#!/usr/bin/python3

"""
Module to list all State objects from the database
hbtn_0e_6_usa that
contain the letter a

"""

if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker
    import sys
    from model_state import Base, State

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2],
                                  sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()

    all_states = session.query(State).filter(State.name.like('%a%')).\
        order_by(State.id)

    for state in all_states:
        print("{}: {}".format(state.id, state.name))
