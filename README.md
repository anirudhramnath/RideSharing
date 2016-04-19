Taxi Ride Sharing
=

Coursework project for Database Management Systems

**Team 6**

 - Srivatsan Muralidharan
 - Chetana Vedantam
 - Vivek Krishnakumar
 - Anirudh Ramnath

----------


Instructions to compile
-------------

**Requirements:**
- Python 2.7.10

Make sure you have pip installed in your machine

*Upgrade pip to latest version*
linux / mac    `$ pip install -U pip`
windows    `python -m pip install -U pip`

*Haversine*
`$ pip install haversine`

*MySQL Python Driver*
`$ pip install MySQL-python`

**Running the simulation:**

The simulation accepts 5 parameters

1. Hub name (Lag_Hub, Penn_Hub, JFK_Hub)
2. Operation hours (peak = p, normal = n, non peak = np)
3. Pool time (It can be any number. example: 7)
4. Passenger distance from each other (example: 5. Which means that passengers who are sharing ride should be dropped off within 5km of each other)
5. Output file name

*Run hotspotAlgorithm.py*

`$ python hotspotAlgorithm.py Lag_Hub p 7 3 output`

The results will be generated in output.txt
