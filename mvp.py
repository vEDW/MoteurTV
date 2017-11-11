#!/usr/bin/python

# -----------------------
# Import required Python libraries
# -----------------------

import RPi.GPIO as GPIO
import time
from flask import Flask, render_template

GPIO.setmode(GPIO.BCM)

#Motor 1 = pins : 17 - 18
#

GPIO_UP = 8
GPIO_DOWN = 11

GPIO.setup(GPIO_UP,GPIO.OUT)
GPIO.setup(GPIO_DOWN,GPIO.OUT)

# Set trigger to False (Low)
GPIO.output(GPIO_UP, False)
GPIO.output(GPIO_DOWN, False)


timelength = 10

def going_UP():
    GPIO.output(GPIO_UP,True)
    time.sleep(timelength)
    GPIO.output(GPIO_UP,False)

def going_DOWN():
    GPIO.output(GPIO_DOWN,True)
    time.sleep(timelength)
    GPIO.output(GPIO_DOWN,False)

app = Flask(__name__)

@app.route("/")
@app.route("/<state>")
def update_robot(state=None):
    if state == 'forward':
        going_UP()
    if state == 'back':
	going_down()
    template_data = {
        'title' : state,
    }
    return render_template('main.html', **template_data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
#GPIO.cleanup()


