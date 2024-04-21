#!/usr/bin/python3
"""
The cities in the states and it 
represent the cities table
"""

from model_state import Base, State
from sqlalchemy import Integer, String, ForeignKey, Column


class City(Base):
    """
    This is the class for cities

    Atttributes:
        id (int): The id of the class
        name (str): The name of the class
        state_id (int): The state the city belongs to
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key = True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable = False)
