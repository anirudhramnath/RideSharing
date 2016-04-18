#! /usr/bin/python

import MySQLdb
from Passenger import Passenger

def fetchValues(table, operation_hours):
  passenger_request_list = [] # list of passenger objects

  # Open database connection
  db = MySQLdb.connect("hurricanes.mysql.uic.edu","smural21","Uic@2015","hurricanes" )

  # prepare a cursor object using cursor() method
  cursor = db.cursor()
  # Prepare SQL query to INSERT a record into the database.
  sql = "SELECT * FROM `%s` WHERE 1" % (table)

  try:
     # Execute the SQL command
     cursor.execute(sql)
     # Fetch all the rows in a list of lists.
     results = cursor.fetchall()

     for row in results:
      passenger_request_list.append(Passenger(row[2], row[10], row[9], row[4]))

  except:
     print "Error: unable to fecth data"

  # disconnect from server
  db.close()

  return passenger_request_list