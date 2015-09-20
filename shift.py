#!/usr/bin/python

import RPi.GPIO as gpio
import time
gpio.setwarnings(0)

clock = 11
latch = 9
data = 10

pins = [clock, latch, data]

gpio.setmode(gpio.BCM)
out = gpio.output

for p in pins:
	gpio.setup(p, gpio.OUT)

byte = 0

def Shift(bits):
	byte = 0
	out(latch, 0)
	while byte < 8:
		for b in bits:
			out(clock, 0)
			if b == '0':
				out(data, 1)
				byte += 1
			else:
				out(data, 0)
				byte += 1
			out(clock, 1)
	out(latch, 1)

Shift("10011010")
time.sleep(5)

gpio.cleanup()
			
