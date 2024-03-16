#!/usr/bin/python3
"""contains the class definition of a State and an instance Base """

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """ Inherits from Base, links to MysQL
        class attribute id: auto generated,
        unique integer, can't be null, primary key
        class attribute name: contain name(max 128 char)
        """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=Flase, primary_key=True)
    name = Column(String(128), nullable=False)
