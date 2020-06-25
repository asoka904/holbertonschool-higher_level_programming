#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    if len(argv) != 4:
        exit()

    username = argv[1]
    password = argv[2]
    database = argv[3]
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password,
                         db=database, charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()