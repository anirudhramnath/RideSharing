#! /usr/bin/env python

class Taxi(object):
    def __init__(self, init_time, dropOfLat, dropOfLong, passenger_count):
        self.init_time = init_time
        self.dropOfLat = [dropOfLat]
        self.dropOfLong = [dropOfLong]
        self.passenger_count = passenger_count