import Rpi.GPIO as GPIO
import time

led =16
sensor=21
GPIO.setmode(GPIO.BCM)
GPIO.setup(led,GPIO.OUT)
GPIO.setup(sensor,GPIO.IN)

while True:
     if(GPIO.input(21)==True):
        print("water detected")
        GPIO.output(led,True)
        time.sleep(1)
    else:
         print("water not detected")
        GPIO.output(led,False)