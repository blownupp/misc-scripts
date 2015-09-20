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

s_dig = ["10000000", "01000000", "00100000", "00010000", "00001000", "00000100", "00000010", "00000001", \
"10000000", "01000000"]

s_num = ["11000000", "11111001", "10100100", "10110000", "10011001", "10010010", "10000010", "11111000", \
"10000000", "10010000"]


def Shift(bits):
	for b in bits:
		out(clock, 0)
		if b == '0':
			out(data, 0)
		else:
			out(data, 1)
		out(clock, 1)
		time.sleep(.000001)

def Multiplex():
	""" Calling it quits for the day, attempting MULTIPLEX
tomorrow, now that I have a semblance of control over the damn
8 digit, 7 segment display...
	"""


index = 0

def Main():
	index = 0
	input = raw_input("Start?\n")
	if input.lower() == ("y" or "yes"):
		while index < 10:
			out(latch, 0)
			for digit in s_dig[index]:
				Shift(digit)
				print digit
			for number in s_num[index]:
				Shift(number[::-1])
				print number
			out(latch, 1)
			time.sleep(.05)
			out(latch, 0)
			for digit in s_dig[index]:
				Shift(digit)
			for number in s_num[index]:
				Shift(number)
			out(latch, 1)
			index += 1
	else:
		time.sleep(.5)
		gpio.cleanup()


Main()		




