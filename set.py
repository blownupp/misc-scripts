import RPi.GPIO as gpio                   # RasPi GPIO
from datetime import datetime       # system time output
import time	 	 	 	 	 	 	 	 	 	 	 	 	 	 	        # sleep
import math                                       # random int generation
# import AdafruitDHT as dht              # DHT11 temp sensor ( *1.8 + 32 = F)

# should work with either a list or a single pin
#def set_pins(pins, io):                      # takes pins and sets to either in or out
#	gpio.setmode(gpio.BCM)
#	for pin in pins:
#		gpio.setup(pin, io)
		
out = gpio.output

class LED(object):
    """ The idea is to be able to pass a list of pins, specify a color
    and have the class make turning on and off the LEDs a lot easier.
    I suppose I'm gping to put the 'waterfall' and 'blinky' routines in here
    as well, so all you have to do is say 'leds.ON('list')' instead of writing
    for loops over and over. """
    leds = []
    def __init__(self, pin):
        self.self = self
        self.pin = pin
		
    def set(self):
        gpio.setmode(gpio.BCM)
        if len(self.pin) > 1:
            for led in self.leds:
                self.leds.append(self.pin)
            gpio.setup(self.leds, gpio.OUT)
        else:
            self.leds.append(self.pin)
            gpio.setup(self.leds, gpio.OUT)    
	
    def ON(self):
        gpio.output(self.leds, True)
	
    def OFF(self):
        gpio.output(self.leds, False)
		
    def blink(self, freq):   # frequency in Hz (5Hz = 5 blinks/sec)
        hertz = 0
        hertz = (int(freq) / 100.0) / 2  # convert to Hz (equal time turned on and off)
        self.ON()                         # so if you want 5 blinks/sec, thats 1 blink
        time.sleep(hertz)     # every .2 sec, so we get .1 sec on, .1 sec off
        self.OFF()
        time.sleep(hertz)


class Sense(object):
    """ Mostly same logic as LED above, except for sensors """
    def __init__(self, pin, type):
        self.self = self
        self.pin = pin
        self.type = type
    
    pass
    


