#!/usr/bin/python3

"""
Module to list the first state object in the database
"""

if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    import sys

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                            format(sys.argv[1], sys.argv[2],
                                     sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker()

    session = Session(bind=engine)

    first_state = session.query(State).first()

    if first_state is None:
        print("Nothing")
    else:
        print("{}: {}".format(first_state.id, first_state.name))

    session.close()
