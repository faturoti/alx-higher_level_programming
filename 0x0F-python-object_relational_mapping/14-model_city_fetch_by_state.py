#!/usr/bin/python3
"""
This program fetches all city object
in the database
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    """
    This gets datafrom cities and states table
    in the database
    """
    db_uri = "mysql+mysqldb://{}:{}@localhost:\
                3306/{}".format(argv[1], argv[2], argv[3])

    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)

    session = Session()

    query = session.query(City, State).join(State)

    for c, s in query.all():
        print("{}: ({:d}) {}".format(s.name, c.id, c.name))

    session.commit()
    session.close()
