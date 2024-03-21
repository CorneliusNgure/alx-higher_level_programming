#!/usr/bin/python3
"""
Displays all values in the states table of the database hbtn_0e_0_usa
that correspond with the provided argument
And ensures safety from SQL injections through parametazation
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()

    query = "SELECT * FROM `states` WHERE BINARY `name` = %s"
    state_name = sys.argv[4]
    c.execute(query, (state_name,))
    [print(state) for state in c.fetchall()]
