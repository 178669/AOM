from tkinter import *
import tkinter as tk
import time
import serial
import re
import math

#from test import StartPage
def controlmotor(target, max):
    '''Motor Notes:
        - 5:1 Gear Ratio [Acryllic]
    '''
    arduino = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=9600,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    timeout=2,
    xonxoff=False,
    rtscts=False,
    dsrdtr=False,
    writeTimeout=5)
    alt = True
    CW, dist = calc(target, max)
    print(CW)
    print(dist)
    if CW == 1:
        try:
            serwrite = "Counter{d}|".format(d = dist)
            arduino.write(serwrite.encode())
            data = arduino.readline()
            if data:
                print(data)
            time.sleep(5)
            #controller.show_frame(StartPage)
        except Exception as e:
            print(e)
            arduino.close()
    if CW == 0:
        try:
            serwrite = "Counter{d}|".format(d = dist)
            arduino.write(serwrite.encode())
            data = arduino.readline()
            if data:
                print(data)
            time.sleep(5)
            #controller.show_frame(StartPage)
        except Exception as e:
            print(e)
            arduino.close()
#function to determine if CW or CCW is faster
#assuming CW is associated with positive positional indicies

def calc(target, max):
    file = open("ArduinoCode/LastIndex.txt", "r")
    current = int(file.read())
    file.close()

    file = open("ArduinoCode/LastIndex.txt", "w")
    file.write(str(target))
    CW = 2

    if current<=2 and target-current>2:
        CW = 0
        distance = abs(target-max)+current
        return (CW, distance)

    elif current>=2 and current-target>=2:
        CW = 1
        distance = abs(current-max)+target
        return (CW, distance)
    else:
        distance = target - current
        if distance>0:
            CW = 1
            return (CW, distance)
        if distance<0:
            CW = 0
            return (CW, abs(distance))
        return (CW, distance)
