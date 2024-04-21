#!/usr/bin/python3
"""
This script defines a State class and
and also define Base class that extends 
the MySQLdb prop.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
    The State class

    Attribute:
        __tablename__ (str): Table name
        id (int): Id for STate
        name (str): The State name
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key = True)
    name = Column(String(128), nullable = False)
