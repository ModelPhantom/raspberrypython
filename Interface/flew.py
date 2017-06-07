import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)

try:
    while True:
        GPIO.output(16,GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(16,GPIO.LOW)
        GPIO.output(12,GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(12,GPIO.LOW)
        GPIO.output(18,GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(18,GPIO.LOW)
        GPIO.output(23,GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(23,GPIO.LOW)
        GPIO.output(24,GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(24,GPIO.LOW)
        GPIO.output(25,GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(25,GPIO.LOW)
    
except KeyboardInterrupt:
    pass
GPIO.cleanup()
