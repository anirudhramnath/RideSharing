#! /usr/bin/env python

class Passenger(object):
    def __init__(self, pickUpTime, destinationLat, destinationLong, passenger_count):
        self.pickUpTime = pickUpTime
        self.destinationLat = destinationLat
        self.destinationLong = destinationLong
        self.passenger_count = passenger_count
