#!/usr/bin/python3
""" defines class City"""
from relationship_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """ class City inherits from Base
    links to the MySQL table cities
    attribute id: unique integer, can't be null auto-generated
        name: string(128), can't be null
    """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
