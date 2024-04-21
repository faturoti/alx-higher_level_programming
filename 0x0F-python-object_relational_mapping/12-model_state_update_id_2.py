#!/usr/bin/python3
"""
to fetch all the states from the 
State table in database
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    This accesses the database vis localhost 
    username and passward @ port 3306
    """
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(argv[1], argv[2], argv[3])
    engine = create_engine(db_uri);
    Session = sessionmaker(bind=engine)
    
    session = Session()

    ret_obj = session.query(State).filter(State.id == '2').first()
    ret_obj.name = 'New Mexico'
    session.commit()
    session.close()
