#!/usr/bin/python3
""" creates the State California with the
    City San Francisco from the database hbtn_0e_100_usa"""
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from models.state import State, Base
from models.city import City
import sys

if __name__ == '__main__':
    engine = create_engine('mysql+mydqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_city = City(name='San Francisco')
    new_state = State(name='California')
    new_state.cities.append(new_city)

    session.add(new_state)
    session.add(new_city)
    session.commit()
