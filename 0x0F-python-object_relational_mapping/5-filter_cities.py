#!/usr/bin/python3
"""the name of state is passed as an argument, list all cities of that state"""
import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("""SELECT cities.name FROM cities INNER JOIN
                states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))
    rows = cur.fetchall()
    temp = list(row[0] for row in rows)
    print(", ".join(temp))
    cur.close()
    db.close()
