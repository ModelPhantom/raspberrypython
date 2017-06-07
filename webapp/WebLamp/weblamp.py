import RPi.GPIO as GPIO
from flask import Flask,render_template,request
app=Flask(__name__)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

pins={
    12:{'name':'yellow 12','state':GPIO.LOW},
    16:{'name':'green 13','state':GPIO.LOW},
    18:{'name':'blue 11','state':GPIO.LOW},
    23:{'name':'red 21','state':GPIO.LOW},
    24:{'name':'yellow 22','state':GPIO.LOW},
    25:{'name':'green 23','state':GPIO.LOW}
    }

for pin in pins:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,GPIO.LOW)

@app.route("/")
def main():
    for pin in pins:
        pins[pin]['state'] = GPIO.input(pin)
        templateData       = {'pins':pins}
    return render_template('main.html',**templateData)

@app.route("/<changePin>/<action>")
def action(changePin,action):
    changePin  = int(changePin)
    deviceName = pins[changePin]['name']
    if action == "on":
        GPIO.output(changePin,GPIO.HIGH)
        message="Turned"+deviceName+"on."
    if action == "off":
        GPIO.output(changePin,GPIO.LOW)
        message="Turned"+deviceName+"off."
    if action == "toggle":
        GPIO.output(changePin,not GPIO.input(changePin))
        message="Toggled"+deviceName+"."

    for pin in pins:
        pins[pin]['state']=GPIO.input(pin)
        templateData={
            'message':message,
            'pins':pins
            }
    return render_template('main.html',**templateData)
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80,debug=True)
    
