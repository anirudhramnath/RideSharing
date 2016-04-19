#! /usr/bin/env python

class Taxi(object):
    def __init__(self, init_time, dropOfLat, dropOfLong,
        passenger_count, distance_traveled, time_traveled):
        self.init_time = init_time
        self.dropOfLat = [dropOfLat]
        self.dropOfLong = [dropOfLong]
        self.passenger_count = passenger_count
        self.distance_traveled = [distance_traveled]
        self.time_traveled = [time_traveled]

