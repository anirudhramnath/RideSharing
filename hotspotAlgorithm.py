#! /usr/bin/env python


import sys
from Taxi import Taxi
import dataFetch
from haversine import haversine
import csv

""" --- Global variables --- """

# list of taxis in the hotspot
taxi_list = [] # type - Taxi object list

# this will be populated from DB
passenger_list = [] # type - Passenger object list

global_time = None # seed the first request's time here

pool_time, operation_hours, HOTSPOT = None, None, None # seed the pool time here

results = [] # list of merged taxis

""" --- END Global variables --- """


def start(hotspot, operationHours, poolTime):
    global global_time, passenger_list, taxi_list, pool_time, operation_hours, results, HOTSPOT

    # Step 1 : Fetch passenger data
    loadValues(hotspot, operation_hours)

    # Step 2 : Update global and pool time
    global_time = passenger_list[0].pickUpTime
    pool_time = int(poolTime)
    operation_hours = operationHours
    HOTSPOT = hotspot

    # Step 3 : Assign users to cabs
    for passenger in passenger_list:
        global_time = passenger.pickUpTime
        assignPassengerToCab(passenger)

    # Step 4 : Dispatch remaining taxis
    for taxi in taxi_list:
        updateResult(taxi)
    taxi_list = []

    # Step 5 : Output the result summary
    summarizeResults()


def loadValues(hotspot, operation_hours):
    global passenger_list
    passenger_list = dataFetch.fetchValues(hotspot, operation_hours)


def checkTimeForEachCab():
    global taxi_list, global_time, pool_time

    dispatched_taxis = [] # will store index of taxis which have been dispatched

    i = 0
    for taxi in taxi_list:
        # Dispatch taxi if capacity is 4 or if it is waiting > pool_time
        if (taxi.passenger_count == 4 or
            global_time - taxi.init_time > pool_time):
            updateResult(taxi)
            dispatched_taxis.append(i)

        i += 1

    # Delete taxis that have been dispatched
    for i in sorted(dispatched_taxis, reverse=True):
        del taxi_list[i]


def summarizeResults():
    global results, pool_time, operation_hours, HOTSPOT

    i = 0
    with open('taxi_trip.txt', 'w') as output:
        output.write("Algorithm ran for hub (%s) during (%s) hours with pool time (%d)\n\n"
                     % (HOTSPOT, operation_hours, pool_time))
        for taxi in results:
            i += 1
            output.write("(%d) %d %d :" % (i, taxi.init_time, taxi.passenger_count))
            output.write(" LAT/LONG => " + str(zip(taxi.dropOfLat, taxi.dropOfLong)))
            output.write("\n")
        output.write("\nTotal number of trips - %d" % (len(results)))


def updateResult(taxi):
    global results
    results.append(taxi)


def assignPassengerToCab(passenger):
    global taxi_list

    if len(taxi_list) == 0:
        taxi = spawnCab(passenger)
        taxi_list.append(taxi)

    else:
        checkTimeForEachCab()
        assigned = False

        for taxi in taxi_list:
            taxi_latlong = (taxi.dropOfLat[0], taxi.dropOfLong[0])
            passenger_latlong = (passenger.destinationLat, passenger.destinationLong)

            # use haversine to calculate the distance
            if (taxi.passenger_count + passenger.passenger_count <= 4
                and haversine(taxi_latlong, passenger_latlong, miles=True) < 3):
                # Here we are assigning just based on passenger count
                taxi.passenger_count = taxi.passenger_count + passenger.passenger_count
                taxi.dropOfLat.append(passenger.destinationLat)
                taxi.dropOfLong.append(passenger.destinationLong)
                assigned = True # set the assigned flag
                break

        if not assigned:
            taxi = spawnCab(passenger)
            taxi_list.append(taxi)


def spawnCab(passenger):
    """ Create a new taxi object and return it """
    return Taxi(passenger.pickUpTime,
                passenger.destinationLat,
                passenger.destinationLong,
                passenger.passenger_count)


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print "Usage - python hotspotAlgorithm.py <hotspot> <operation_hours = p|n|np> <pool time>"
        exit()
    hotspot = sys.argv[1]
    operation_hours = sys.argv[2]
    pool_time = sys.argv[3]

    start(hotspot, operation_hours, pool_time)