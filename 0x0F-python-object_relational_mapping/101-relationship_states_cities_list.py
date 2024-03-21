#!/usr/bin/python3
"""lists all State objects, and corresponding City objects
    contained in the database hbtn_0e_101_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State, Base
from relationship_city import City

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata(create_engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for ins in session.query(State).order_by(state.id):
        print("{}: {}".format(str(ins.id), ins.name))
        for ins_city in ins.cities:
            print("    {}: {}".format(str(ins_city.id), ins_city.name))
