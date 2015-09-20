#!/usr/bin/python

""" Hopefully a successful test with my 7 segment 8 digit display
using 74HC595 shift registers. Following a positive result, this
will integrate with the ESP8266 and show the status of the PIR? 
Maybe the relay? Ultrasonic? Anyway, I'm having too much trouble
trying to learn Lua at the moment, the interpreter isn't even
accepting scripts more experienced developers have written.

So without further adieu, let's play.
"""

#---- Import modules ----#
import RPi.GPIO as gpio
from datetime import datetime
from datetime import time
import math

#--- Setup pins...---#
gpio.setwarnings(0)
gpio.setmode(gpio.BCM)

sck = 9
di0 = 10
rck = 11
#--- Corrusponds to MOSI MISO and SCLK ---#
pins = [sck, di0, rck]

for p in pins:
	gpio.setup(p, gpio.OUT)

#--- Setup all 3 pins, set all 3 LOW ---#

""" So the idea of Shiftout() is you give the function 8 bits
of data and it clocks it into the register. For the 595 to accept
the data, di0 is set low, followed by rck then sck. For each bit,
sck will go HIGH then LOW for each bit di0 contains. If di0 starts
with a 0, sck will start low with di0, di0 will stay low for another
clock pulse while sck goes HIGH. This tells the 595 that we're sending
a 0 for it to store. For a 1, it's the same concept only di0 is HIGH.

The whole time this is happening, rck is LOW, and stays LOW until
we're done clocking in data. Once the 8 (16?) bits are sent,
we set rck HIGH for the 595 to shift the data out. """

# count = 0  # initially 0, up through 7 in the following loop

def ShiftOut(bits):  # we'll run this later inside a loop to multiplex
	gpio.output(rck, 0) # latch is low, ready for data
	for b in bits:
		gpio.output(sck, 0) # set clock before sending bit
		if b == "0":
			gpio.output(di0, 1) # 595 polarity is HIGH
		else:                       # so HIGH = 0
			gpio.output(di0, 0) # likewise, LOW = 1
		gpio.output(sck, 1) # finish clock cycle
		print b
	gpio.output(rck, 1) # once data is in, latch HIGH to show

#--- That's too simple to work... ---#

numbers = []

def Main():
	print "Alright, time to figure out this display\n"
	test_input = bin(raw_input("Enter some 1's and 0's...\n"))
	test_int = 8 - test_input.bit_length()
	if test_int > 0:
		numbers.append((test_input << test_int))
	else:
		numbers.append(test_input)
	print "Want to input more?\n"
	test_input = raw_input("Y or N").lower()
	if test_input == ("y" or "yes"):
		Main()
	else:
		try:
			for num in numbers:
				print "Shifting " + num + " ..."
				ShiftOut(num)
				time.sleep(5)
			Main()
		except:
			while 1:
				print "I guess that didn't go as planned :("
				ex_var = raw_input("Try again?\n")
				if ex_var.lower() == ("y" or "yes"):
					Main()
					break
				elif ex_var.lower() != ("n" or "no"):
					print "Didn't quite catch that..."
					time.sleep(1)
					gpio.cleanup()
					exit()
				else:
					gpio.cleanup()
					exit()

Main()

