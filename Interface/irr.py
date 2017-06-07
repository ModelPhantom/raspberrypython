#!/usr/bin/python

import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(25,GPIO.OUT)

freq=38000 #freq = 38kHz
dc=1/3 #duty cycle 1:3

bit38k=1/freq

bit560=0.000560

bit1690=0.001690

bit9ms=0.009

bit4d5ms=0.0045

bit2d25ms=0.00225



p1=GPIO.PWM(4,freq) #output as channel 4


try:
    #logical 1
    def logical1():
        #send 560us HIGH
        for implus in range(0,bit560,bit38k):
            p1.changeDutyCycle(100)
            time.sleep(bit38k)
            
        #send 690us LOW
        p1.changeDutyCycle(dc)
        time.sleep(bit1690)
        return

    #logical 0
    def logical0():
        #send 560us HIGH
        for implus in range(0,bit560,bit38k):
            p1.changeDutyCycle(100)
            time.sleep(bit38k)
            
        #send 560us LOW
        p1.changeDutyCycle(dc)
        time.sleep(bit560)
        return

    #NEC Header
    def NEC_Header():
        #send 9ms HIGH
        for implus in range(0,bit9ms,bit38k):
            p1.changeDutyCycle(100)
            time.sleep(bit38k)
            
        #send 4.5ms LOW
        p1.changeDutyCycle(dc)
        time.sleep(bit4d5ms)
        return
        
    
    #NEC Endder
    def NEC_Endder():
        #send 9ms HIGH
        for implus in range(0,bit9ms,bit38k):
            p1.changeDutyCycle(100)
            time.sleep(bit38k)
        #send 2.25ms LOW
        p1.changeDutyCycle(dc)
        time.sleep(bit2d25ms)
        #send 560ms HIGH
        for implus in range(0,bit560,bit38k):
            p1.changeDutyCycle(100)
            time.sleep(bit38k)
        
        p1.changeDutyCycle(dc)
        return
        

    #NEC Repeat
    def NEC_Repeat():
        for implus in range(0,bit9ms,bit38k):
            p1.changeDutyCycle(100)
            time.sleep(bit38k)
        for implus in range(0,bit2d25ms,bit38k):
            p1.changeDutyCycle(dc)
            time.sleep(bit38k)
        for implus in range(0,bit560,bit38k):
            p1.changeDutyCycle(100)
            time.sleep(bit38k)
        
        p1.changeDutyCycle(dc)
        return
            
    #Stand NEC 6121 with system code 01FD
    def Code1_Menu():
        p1.start(dc) #set duty-cycle
        NEC_Header;
        #01FD
        logical0;
        logical0;
        logical0;
        logical0;
        logical0;
        logical0;
        logical0;
        logical1;
        
        logical1;
        logical1;
        logical1;
        logical1;
        logical1;
        logical1;
        logical0;
        logical1;
        
        #80
        logical1;
        logical0;
        logical0;
        logical0;
        logical0;
        logical0;
        logical0;
        logical0;
        
        
        #~80
        logical0;
        logical1;
        logical1;
        logical1;
        logical1;
        logical1;
        logical1;
        logical1;
        
        NEC_Endder;
        p1.stop()
        return
    
    for operations in range(0,100,1):
        Code1_Menu;
        
except KeyboardInterrupt:
    pass

GPIO.cleanup()
