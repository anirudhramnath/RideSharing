#! /usr/bin/env python

from subprocess import call

hotspot=['JFK_Hub', 'Lag_Hub', 'Penn_Hub']
pool_time=["3", "5", "7", "10", "15", "20"]
hours = ["p", "np", "n"]
radius = map(str, range(3, 6))

for hspot in hotspot:
    for pt in pool_time:
        for hrs in hours:
            for rad in radius:
                call(["python","hotspotAlgorithm.py", hspot, hrs, pt, rad, "results/h%s_o%s_pt%s_r%s" % (hspot, hrs, str(pt),str(rad))])


