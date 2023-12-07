from tkinter import *
import tkinter as tk
import time
import serial
import re
import math

#from test import StartPage
portarr = ['/dev/ttyUSB0', 'COM4']
HPorJetson = 0
def controlmotor(target, max):
    '''Motor Notes:
        - 5:1 Gear Ratio [Acryllic]
    '''
    arduino = serial.Serial(
    port=portarr[HPorJetson],
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

def calc(target, maxi):
    file = open("ArduinoCode/LastIndex.txt", "r")
    current = int(file.read())
    file.close()

    file = open("ArduinoCode/LastIndex.txt", "w")
    file.write(str(target))
    CW = 2
    #switch case for most optimal path for rotation b/c I don't want to think anymore :)
    if 2 >= target-current > 0:
        CW = 1
        distance = target-current
        return CW, distance
    elif target-current == 0:
        return 2, 0
    elif target-current<0 and abs(target-current)<=2:
        CW = 0
        distance = abs(target-current)
        return CW, distance
    elif current >= 4 and target == 5:
        CW = 1
        distance = target - current
        return CW, distance
    elif current >= 4 and target == 1:
        CW = 1
        distance = maxi-current + target
        return CW, distance
    else:
        CW = 0
        distance = abs(maxi-target)+current
        return CW, distance
