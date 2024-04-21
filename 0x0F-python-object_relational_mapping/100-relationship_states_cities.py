#!/usr/bin/python3
"""
To create a State and City then
send to the Dtabase
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    """
    This is th access the database and create engine
    to help send request to database
    """

    db_uri = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    engine = create_engine(db_uri)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    obj_state = State(name='California')
    obj_city = City(name='San Francisco')
    obj_state.cities.append(obj_city)

    session.add(obj_state)
    session.commit()
    session.close()
