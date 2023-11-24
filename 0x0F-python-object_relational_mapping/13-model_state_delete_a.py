#!/usr/bin/python3

"""
Deletes all State objects with a name containing the letter 'a' from the
database hbtn_0e_6_usa
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
        session.delete(state)

    session.commit()

    session.close()
