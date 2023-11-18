#!/usr/bin/python3

"""Module to list all cities from the database hbtn_0e_0_usa
"""

if __name__ == "__main__":
    import MySQLdb as sql
    from sys import argv
    conn = sql.connect(host="localhost", user=argv[1],
                       passwd=argv[2], db=argv[3], port=3306)

    cursor = conn.cursor()
    cursor.execute(
        """SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states
        ON states.id = cities.state_id
        ORDER BY cities.id ASC"""
    )

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    conn.close()
