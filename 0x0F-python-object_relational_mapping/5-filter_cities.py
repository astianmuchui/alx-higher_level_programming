#!/usr/bin/python3

"""Module to list all cities from the database hbtn_0e_0_usa
that match the argument provided
"""

if __name__ == "__main__":
    import MySQLdb as sql
    from sys import argv
    conn = sql.connect(host="localhost", user=argv[1],
                       passwd=argv[2], db=argv[3], port=3306)

    cursor = conn.cursor()
    cursor.execute(
        """SELECT cities.name
        FROM cities
        JOIN states
        ON states.id = cities.state_id
        WHERE states.name = %s
        ORDER BY cities.id ASC""", (argv[4],)
    )

    cities = [row[0] for row in cursor.fetchall()]
    print(', '.join(cities))

    cursor.close()
    conn.close()
