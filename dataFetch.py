#! /usr/bin/env python

import MySQLdb
from Passenger import Passenger

def fetchValues(table, operation_hours):
  passenger_request_list = [] # list of passenger objects

  # Open database connection
  db = MySQLdb.connect("hurricanes.mysql.uic.edu","smural21","Uic@2015","hurricanes" )

  # prepare a cursor object using cursor() method
  cursor = db.cursor()

  # Prepare SQL query to SELECT a record into the database.

  from_time1, to_time1, from_time2, to_time2 = None, None, None, None

  if table == "JFK_Hub":
    if operation_hours == "p":
      from_time1, to_time1 = "13", "17"
      from_time2, to_time2 = "21", "23"
    elif operation_hours == "np":
      from_time1, to_time1 = "01", "04"
      from_time2, to_time2 = "01", "04"
    elif operation_hours == "n":
      from_time1, to_time1 = "11", "14"
      from_time2, to_time2 = "18", "20"
  elif table == "Penn_Hub":
    if operation_hours == "p":
      from_time1, to_time1 = "11", "15"
      from_time2, to_time2 = "21", "23"
    elif operation_hours == "np":
      from_time1, to_time1 = "02", "07"
      from_time2, to_time2 = "02", "07"
    elif operation_hours == "n":
      from_time1, to_time1 = "07", "11"
      from_time2, to_time2 = "07", "11"
  elif table == "Lag_Hub":
    if operation_hours == "p":
      from_time1, to_time1 = "13", "18"
      from_time2, to_time2 = "20", "23"
    elif operation_hours == "np":
      from_time1, to_time1 = "01", "05"
      from_time2, to_time2 = "01", "05"
    elif operation_hours == "n":
      from_time1, to_time1 = "09", "12"
      from_time2, to_time2 = "09", "12"

  sql = "SELECT * FROM `%s` WHERE SUBSTR(Pickup_Datetime, -5, 2) between \
        %s and %s or SUBSTR(Pickup_Datetime, -5, 2) between \
        %s and %s ORDER BY SUBSTR(Pickup_Datetime, -5) LIMIT 9999999" % (table, from_time1,
        to_time1, from_time2, to_time2)

  try:
    # Execute the SQL command
    cursor.execute(sql)
    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()

    for row in results:
      passenger_request_list.append(Passenger(row[2], row[10], row[9], row[4], row[6], row[5]))

  except:
     print "Error: unable to fecth data"

  # disconnect from server
  db.close()

  return passenger_request_list