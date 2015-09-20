#!/usr/bin/python

import urllib2
from datetime import timedelta
import RPi.GPIO as io
import datetime
import time
# import SDL_DS3231 # system time is already on ds3231

# init variables & misc. pins
io.setup(io.BCM)

pirPin = 9
relayPin = 10

relayState = 0
pirTimer = 0
lowerBound = (.25 * 3.325)

io.mode(pirPin, io.IN)
io.mode(relayPin, io.OUT)

pirState = io.input
flipRelay = io.output
timeDel = datetime.timedelta
lumin = urllib2.urlopen("https://api.thingspeak.com/channels/50301/fields/5/last").read()

# control flow functions - 
#  When lower boundary is TRUE and PIR is TRUE, init relayPin
# for $time, probably based upon PIR retriggering...

""" 

  test_the_waters() will test the conditions to determin
if the relay should be set ON or OFF; ambient brightness, occupancy,
time etc. returns:

   a) darker than lower bound
   b) is occupied
   c) after local sundown

should return any combination of the 3 depending on conditions 

"""

def test_the_waters():
    conditions = []
    if (sensorDat <= lowerBound) and (pirState(pirPin) and datetime.datetime.now() >= timeDel(hours=19)): # pir timer since triggered?
        conditions.append("a", "b", "c")
    elif 
        return "b"
    elif datetime.datetime.now() >= timeDel(hours=19):
        return "c"
    



# need to get more setup first, lets do an outline
# to help map out control sequence...

def testRelay():
    if relayState != 1 and isTrue():
        flipRelay(relayPin, 1)
        relayState = 1
    elif relayState == 1 or (isTrue() == False):
        flipRelay(pirPin, 0)
        relayState = 0

# get data from esp8266 and/or thingspeak field 5
def readLevel():
    pass


# keep track of whether the room is occupied or not,
# no reason to waste electricity!
def setOccupance():
    pirTimer = datetime.datetime.now()
    if pirTimer <= timeDel(minutes=15):
        pirTimer = datetime.datetime.now()
    elif pirTimer > timeDel(minutes=15):
        setRelay()
        pirTimer = datetime.datetime.now()

def flipRelay():
    if relayState == 0:
        flipRelay(relayPin, 1)
        relayState = 1
    else:
        flipRelay(relayPin, 0)
        relayState = 0


        
