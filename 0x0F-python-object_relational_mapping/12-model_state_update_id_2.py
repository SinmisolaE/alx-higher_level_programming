#!/usr/bin/python3
""" changes the name of a State object from the database
    where id = 2, name to New Mexico
    """
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new = "New Mexico"
    ins = session.query(State).filter_by(id=2).first()
    ins.name = new
    session.commit()
