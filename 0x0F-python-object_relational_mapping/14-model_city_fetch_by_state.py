#!/usr/bin/python3
""" prints all City objects from database 'hbtn_0e_14_usa'
    display '<state name>: <city id> <city name>'
    """
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    session = Session()
    for ins in (session.query(State.name, City.id, City.name)
                .filter(State.id == City.state_id)):
        print(ins[0] + ": (" + str(ins[1]) + ") " + ins[2])
