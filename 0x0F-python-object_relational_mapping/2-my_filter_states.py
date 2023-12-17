#!/usr/bin/python3
"""
Script that displays all values in the states table of hbtn_0e_0_usa where name matches the argument
"""
import MySQLdb
import sys

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306,
            user=sys.argv[1], passwd=sys.argv[2],
            db=sys.argv[3], charset="utf8")
    cr = db.cursor()
    myQuery = " ".join([
        "SELECT * FROM states",
        "WHERE name LIKE BINARY '{}'",
        "ORDER BY id ASC",
        ]).format(sys.argv[4])
    cr.execute(myQuery)
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    db.close()
