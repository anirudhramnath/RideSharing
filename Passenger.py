#! /usr/bin/env python

class Passenger(object):
    def __init__(self, pickUpTime, destinationLat, destinationLong, passenger_count):

        hours = int(pickUpTime.split()[1].split(":")[0])
        mins = int(pickUpTime.split()[1].split(":")[1])

        self.pickUpTime = ( 60*hours ) + mins
        self.destinationLat = destinationLat
        self.destinationLong = destinationLong
        self.passenger_count = passenger_count
