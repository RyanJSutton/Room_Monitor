__author__ = 'Ryan Sutton'

from bottle import Bottle, template, run, route
import serial
import time

application = Bottle()

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=10)

@application.route('/gettemp')
def return_temp():
    ser.flushOutput()
    ser.flushInput()
    ser.flush()
    while True:
        temp = ser.readline()
        tempStripped = str(temp.strip())
        if tempStripped != "b''":
            tempStripped = float(tempStripped[2:-1])
            print(tempStripped)
            break
    return template('temp', {'temperature': str(tempStripped)})

@application.route('/gettempjson')
def temp_json():
    while True:
        ser.flushOutput()
        ser.flushInput()
        ser.flush()
        temp = ser.readline()
        tempStripped = str(temp.strip())
        if tempStripped != "b''":
            tempStripped = float(tempStripped[2:-1])
            print(tempStripped)
            break
    return {'temp': str(tempStripped)}

@application.route('/')
def index():
    return '<a href="/gettemp">Get Temperature</a>'

if __name__ == '__main__':
    application.run(debug=True, port=49090)