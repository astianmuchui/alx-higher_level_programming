#!/usr/bin/python3

"""Module to list all states from the database hbtn_0e_0_usa
Matching a param
"""

if __name__ == "__main__":
    import MySQLdb as sql
    from sys import argv
    conn = sql.connect(host="localhost", user=argv[1],
                       passwd=argv[2], db=argv[3], port=3306)

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM `states` WHERE name\
                   LIKE BINARY '%{}%' ORDER BY `states`.`id` ASC"
                   .format(argv[4]))

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    conn.close()
