#!/usr/bin/python3

"""Module to list all states from the database hbtn_0e_0_usa
"""

if __name__ == "__main__":
    import MySQLdb as sql
    from sys import argv
    import sqlalchemy as orm

    conn = orm.connect(host="localhost", user=argv[2],
                       passwd=argv[3], db=argv[4], port=3306)

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    conn.close()
