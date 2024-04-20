#!/usr/bin/python3
"""
The code shows the list of entries in state
and cities tables
table in database(hbtn_0e_0_usa) .
"""


import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Tries to access the tables in the database 
    and creates the connection first
    and then helps to conenct to cities
    """
    db = MySQLdb.connect(host="localhost",
                            user = argv[1],
                            port = 3306,
                            passwd = argv[2],
                            db = argv[3])

    with db.cursor() as cur:
        cur.execute("""
                    SELECT 
                        cities.id, cities.name
                    FROM 
                        cities
                    JOIN
                        states
                    ON
                        cities.state_id = states.id
                    WHERE
                        states.name LIKE BINARY %(statename)s
                    ORDER BY
                        cities.id ASC
                """, {
                        'statename' : argv[4]
                    })
                    
        rows = cur.fetchall()

    if rows is not None:
        print(", ".join([row[1] for row in rows]))
