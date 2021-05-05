import serial
import json
import time
import math

sensor = {}

def writeJSON(data):    
    with open('sensor_data.json', 'w') as fp:
        json.dump(data, fp)


def calcVolume(height, radius):
    print(height)
    return int(round(math.pi*(30-height)*radius**2, 0))


ser = serial.Serial('/dev/ttyACM0', 9600)

i = 0

while (True): 
    if(ser.in_waiting > 0):
        line = str(ser.readline())
        # print(line)
        if "distance" in line:
            volume = calcVolume(int(line.split(" ") [2]), 5)
            sensor ['volume'] = volume
        elif "Celcius" in line:
            temp = round(float(line.split(" ") [1]), 1)
            sensor ['temperature'] = temp
        writeJSON(sensor)

    