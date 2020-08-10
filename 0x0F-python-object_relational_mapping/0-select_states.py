#!/usr/bin/python3
#Lists all states from the database

import MySQLdb
import sys


if __name__ == '__main__':

    db_host = "localhost"
    user = sys.argv[1]
    pswd = sys.argv[2]
    db_name = sys.argv[3]

    conn = MySQLdb.connect(host=db_host,
                           port=3306,
                           user=user,
                           passwd=pswd,
                           db=db_name,
                           charset="utf8")

    cur = conn.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()

    for data in rows:
        print(data)
    conn.close()
    cur.close()
