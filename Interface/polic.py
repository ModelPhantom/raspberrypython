import RPi.GPIO as GPIO
import time

 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

try:
    while True:
        GPIO.output(23,GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(23,GPIO.LOW)
        GPIO.output(18,GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(18,GPIO.LOW)
        time.sleep(0.3)
    
        GPIO.output(23,GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(23,GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(23,GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(23,GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(18,GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(18,GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(18,GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(18,GPIO.LOW)
        time.sleep(0.3)
    
except KeyboardInterrupt:
    pass
GPIO.cleanup()
