from datetime import datetime
import RPi.GPIO as io
import time
import Adafruit_DHT

io.set_warnings = False

pir = 26
on = [17, 24, 12, 27]
off = 22
s_on = io.output

io.setmode(io.BCM)
io.setup(26, io.IN)
io.setup(on, io.OUT)
io.setup(22, io.OUT)
io.setup(27, io.OUT)

l_on = io.output

def GetWeather():
    humidity, temp = Adafruit_DHT.read_retry(11, 13)   # (DHT11, PIN#)
    temperature = (float(temp) * 1.8) + 32
    return "Current conditions: %d *F, %d %\ RH" % (temperature, humidity)

def LogTime(time):
    f = open("pir-log.txt", "a")
    f.write("\nMotion @ " + str(time))
    f.close()

def Motion(pir):
    start = time.time()
    now = datetime.now()
    print "\nMotion detected!"
    print "Logged at: %s:%s:%s" % (now.hour, now.minute, now.second)
    print "\n" + str(GetWeather())
    LogTime(now)
    while time.time() - start < 5:
        l_on(on, True)
        time.sleep(.05)
        l_on(on, False)
        time.sleep(.1)
#        for i in range(10):
#            for x in range(4):
#                time.sleep(.1)
#                s_on(27, 1)
#                time.sleep(.05)
#                s_on(27, 0)
#            time.sleep(.125)

    
print "PIR test, active state: " + str(pir)
time.sleep(2)
print "Ready" + "." * 10

try:
	io.add_event_detect(pir, io.RISING, callback=Motion)
	while 1:
            print ".",
            l_on(on, 0)
            l_on(22, 1)
            time.sleep(.2)
            l_on(22, 0)
            time.sleep(5)
except KeyboardInterrupt:
    print "Quit"
    io.cleanup()
