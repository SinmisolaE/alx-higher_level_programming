#!/usr/bin/python3
""" takes in argument and displays all values where name matche the argument
    It should be safe from SQL injection"""
import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    search = sys.argv[4]
    cur.execute("SELECT * FROM states WHERE name LIKE %s", (search, ))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
