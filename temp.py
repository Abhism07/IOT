import  Adafruit_DHT
import time
import Rpi.GPIO as GPIO
led=16
sensor=20
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor,GPIO.IN)
GPIO.setup(led,GPIO.OUT)
while True:
   humidity,tempereture = Adafruit_DHT.read_retry(11,20)
   print(temperature,humidity)
   time.sleep(1)
   if(humidity >50):
          GPIO.input(sensor)
           GPIO.output(led,True)
   else:
          GPIO.output(led,False)
   