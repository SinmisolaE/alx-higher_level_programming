#!/usr/bin/python3
""" deletes all States objects with a name containing letter 'a'"""
import sys
from models_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    ins = session.query(State).filter(State.name.like('%a%'))
    for each_ins in ins:
        session.delete(each_ins)
    session.commit()
