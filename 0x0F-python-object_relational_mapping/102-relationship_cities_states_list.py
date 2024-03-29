#!/usr/bin/python3
""" lists all City objects from the database hbtn_0e_101_usa"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_city import City
from relationship_state import State, Base

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for ins in session.query(State).order_by(State.id):
        for ins_city in ins.cities:
            print("{}: {} -> {}".format(ins_city.id, ins_city.name, ins.name))
