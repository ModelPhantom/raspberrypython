import RPi.GPIO as GPIO
import time

 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)

try:
    GPIO.output(23,GPIO.HIGH)
    GPIO.output(24,GPIO.HIGH)
    GPIO.output(25,GPIO.HIGH)
    time.sleep(3)
    GPIO.output(23,GPIO.LOW)
    GPIO.output(24,GPIO.LOW)
    GPIO.output(25,GPIO.LOW)
    time.sleep(1)
    
    while True:
        GPIO.output(25,GPIO.HIGH)
        time.sleep(5)
        GPIO.output(25,GPIO.LOW)
        time.sleep(0.3)
        GPIO.output(25,GPIO.HIGH)
        time.sleep(0.3)
        GPIO.output(25,GPIO.LOW)
        time.sleep(0.3)
        GPIO.output(25,GPIO.HIGH)
        time.sleep(0.3)
        GPIO.output(25,GPIO.LOW)
        time.sleep(0.3)
        GPIO.output(25,GPIO.HIGH)
        time.sleep(0.3)
        
        GPIO.output(24,GPIO.HIGH)
        GPIO.output(25,GPIO.LOW)
        time.sleep(0.3)
        GPIO.output(24,GPIO.LOW)
        time.sleep(0.3)
        GPIO.output(24,GPIO.HIGH)
        time.sleep(0.3)
        GPIO.output(24,GPIO.LOW)
        time.sleep(0.3)
        GPIO.output(24,GPIO.HIGH)
        time.sleep(0.3)
        GPIO.output(24,GPIO.LOW)
        time.sleep(0.3)
        GPIO.output(24,GPIO.HIGH)
        time.sleep(0.3)
        GPIO.output(24,GPIO.LOW)
        time.sleep(0.1)

        GPIO.output(23,GPIO.HIGH)
        time.sleep(3)
        GPIO.output(23,GPIO.LOW)
        time.sleep(0.3)
        GPIO.output(23,GPIO.HIGH)
        time.sleep(0.3)
        GPIO.output(23,GPIO.LOW)
        time.sleep(0.3)
        GPIO.output(23,GPIO.HIGH)
        time.sleep(0.3)
        GPIO.output(23,GPIO.LOW)
        time.sleep(0.1)
        
except KeyboardInterrupt:
    pass
GPIO.cleanup()
