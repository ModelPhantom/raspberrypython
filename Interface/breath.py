import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(12,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)

GPIO.setwarnings(False)

freqscan=1000
freq=100
step=10
sleeptime=0.05

p1=GPIO.PWM(16,freqscan)
p2=GPIO.PWM(12,freqscan)
p3=GPIO.PWM(18,freqscan)
p4=GPIO.PWM(23,freqscan)
p5=GPIO.PWM(24,freqscan)
p6=GPIO.PWM(25,freqscan)

p1.start(0)
p2.start(0)
p3.start(0)
p4.start(0)
p5.start(0)
p6.start(0)

try:
    while True:
        for dc in range(0,freq+1,step):
            p1.ChangeDutyCycle(dc)
            time.sleep(sleeptime)
        for dc in range(freq,-1,-step):
            p1.ChangeDutyCycle(dc)
            time.sleep(sleeptime)
            
        for dc in range(0,freq+1,step):
            p2.ChangeDutyCycle(dc)
            time.sleep(sleeptime)
        for dc in range(freq,-1,-step):
            p2.ChangeDutyCycle(dc)
            time.sleep(sleeptime)
            
        for dc in range(0,freq+1,step):
            p3.ChangeDutyCycle(dc)
            time.sleep(sleeptime)
        for dc in range(freq,-1,-step):
            p3.ChangeDutyCycle(dc)
            time.sleep(sleeptime)
            
        for dc in range(0,freq+1,step):
            p4.ChangeDutyCycle(dc)
            time.sleep(sleeptime)
        for dc in range(freq,-1,-step):
            p4.ChangeDutyCycle(dc)
            time.sleep(sleeptime)
            
        for dc in range(0,freq+1,step):
            p5.ChangeDutyCycle(dc)
            time.sleep(sleeptime)
        for dc in range(freq,-1,-step):
            p5.ChangeDutyCycle(dc)
            time.sleep(sleeptime)
            
        for dc in range(0,freq+1,step):
            p6.ChangeDutyCycle(dc)
            time.sleep(sleeptime)
        for dc in range(freq,-1,-step):
            p6.ChangeDutyCycle(dc)
            time.sleep(sleeptime)
except KeyboardInterrupt:
    pass
p1.stop()
p2.stop()
p3.stop()
p4.stop()
p5.stop()
p6.stop()

GPIO.cleanup()
