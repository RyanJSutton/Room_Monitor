__author__ = 'Ryan Sutton'

from bottle import Bottle, template, run, route
import serial
import time

application = Bottle()

ser = serial.Serial('COM3', 9600, timeout=50)

@application.route('/gettemp')
def return_temp():
    if ser:
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
    if ser:
        while True:
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