#!/usr/bin/env python
import sqlite3
import datetime

# CONSTANTS
DB = 'jrv.db'
TABLE = 'queue'

# Connexion with the database and creation of the cursor object
conn = sqlite3.connect(DB)
c = conn.cursor()

# Building the event
date = datetime.datetime.now()
type = "test"
message = "this is a test"

# Building the query
q = "INSERT INTO %s VALUES (\"%s\", \"%s\", \"%s\");" % (TABLE, date, type, message)

# Inserting the test object into the database
c.execute(q)

# Send a query to get all the data and print it to see if our query worked
c.execute("SELECT * FROM queue WHERE date=\"%s\" AND type=\"%s\" AND message=\"%s\";" % (date, type, message))
print 'Resultado:'
for row in c:
    print row

# Commit the changes to the database
conn.commit()
conn.close()