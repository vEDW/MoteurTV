#!/usr/bin/python

# -----------------------
# Import required Python libraries
# -----------------------

import explorerhat
import time
from flask import Flask, render_template

timelength = 1

def going_Left():
    explorerhat.motor.one.forward()
    time.sleep(timelength)
    explorerhat.motor.one.stop()

def going_Right():
    explorerhat.motor.one.backward()
    time.sleep(timelength)
    explorerhat.motor.one.stop()

app = Flask(__name__)

@app.route("/")
@app.route("/<state>")
def update_robot(state=None):
    if state == 'left':
        going_Left()
    if state == 'right':
	going_Right()
    template_data = {
        'title' : state,
    }
    return render_template('main.html', **template_data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
