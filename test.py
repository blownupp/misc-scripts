from set import LED
import time

blue = [22, 25]
red = [23, 12, 9]
green = [10, 16, 24]

blue, red, green = LED(blue), LED(red), LED(green)

blue = blue.LED(blue)
red = LED(red)
aaa = LED(green)
ass.set()
red.set()
blue.set()
red.blink(10)
blue.blink(5)
aaa.blink(25)
time.sleep(1)

time.sleep(5)

blue.OFF()
red.OFF()
aaa.OFF()

