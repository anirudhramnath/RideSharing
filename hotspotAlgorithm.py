#! /usr/bin/env python


import sys
from Taxi import Taxi
import dataFetch
from haversine import haversine
from pprint import pprint

""" --- Global variables --- """

# list of taxis in the hotspot
taxi_list = [] # type - Taxi object list

# this will be populated from DB
passenger_list = [] # type - Passenger object list

global_time = None # seed the first request's time here

pool_time = None # seed the pool time here

results = []

""" --- END Global variables --- """


def start(hotspot, operation_hours, poolTime):
    global global_time, passenger_list, taxi_list, pool_time, results

    # Step 1 : Fetch passenger data
    loadValues(hotspot, operation_hours)

    # Step 2 : Update global and pool time
    global_time = passenger_list[0].pickUpTime
    pool_time = poolTime

    # Step 3 : Assign users to cabs
    ##TODO: Distance calculation
    for passenger in passenger_list:
        global_time = passenger.pickUpTime
        assignPassengerToCab(passenger)

    # Step 4 : Dispatch remaining taxis
    for taxi in taxi_list:
        updateResult(taxi)
    taxi_list = []

    print "TOTAL NO OF TRIPS IS", str(len(results))


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


def calulateRouteDistance():
    pass


def updateResult(taxi):
    global results
    results.append(taxi)
    #print "Taxi dispatched. init_time =", taxi.init_time, "passenger_lat_long =", (taxi.dropOfLat, taxi.dropOfLong)


def assignPassengerToCab(passenger):
    global taxi_list

    if len(taxi_list) == 0:
        taxi = Taxi(passenger.pickUpTime,
                    passenger.destinationLat,
                    passenger.destinationLong,
                    passenger.passenger_count)
        taxi_list.append(taxi)

    else:
        checkTimeForEachCab()
        assigned = False

        for taxi in taxi_list:
            taxi_latlong = (taxi.dropOfLat[0], taxi.dropOfLong[0])
            passenger_latlong = (passenger.destinationLat, passenger.destinationLong)

            # use haversine to calculate the distance
            if (taxi.passenger_count + passenger.passenger_count <= 4
                and haversine(taxi_latlong, passenger_latlong, miles=True) < 0.1):
                # Here we are assigning just based on passenger count
                taxi.passenger_count = taxi.passenger_count + passenger.passenger_count
                taxi.dropOfLat.append(passenger.destinationLat)
                taxi.dropOfLong.append(passenger.destinationLong)
                assigned = True # set the assigned flag
                break

        if not assigned:
            taxi = Taxi(passenger.pickUpTime,
                    passenger.destinationLat,
                    passenger.destinationLong,
                    passenger.passenger_count)
            taxi_list.append(taxi)


def spawnCab():
    pass


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print "Usage - python hotspotAlgorithm.py <hotspot> <operation_hours = p|n|np> <pool time>"
        exit()
    hotspot = sys.argv[1]
    operation_hours = sys.argv[2]
    pool_time = sys.argv[3]

    start(hotspot, operation_hours, pool_time)