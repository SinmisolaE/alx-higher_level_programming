#!/usr/bin/python3
""" lists all State objects with name passed as argument
    should display the states.id
    """
import sys
from models_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metabase.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    ins = session.query(State).filter(State.name == (sys.argv[4],))
    try:
        print(ins[0].id)
    except IndexError:
        print("Not found")
