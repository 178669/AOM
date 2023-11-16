from tkinter import *
import tkinter as tk
import time
import serial
import re
#from test import StartPage
def controlmotor(target, max):
    '''Motor Notes:
        - 10:1 Gear Ratio [Wood Gear]
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
    CW, dist = calc(5, 5)
    print(dist)
    if CW == 0:
        try:
            serwrite = "Counter{d}|".format(d = dist)
            arduino.write(serwrite.encode())
            data = arduino.readline()
            if data:
                print(data)
                alt = True
            time.sleep(5)
            #controller.show_frame(StartPage)
        except Exception as e:
            print(e)
            arduino.close()
#function to determine if CW or CCW is faster
#assuming CW is associated with positive positional indicies

def calc(target, max):
    if current<=3 and target-current>3:
        CW = 0
        distance = abs(target-max)+current
        return (CW, distance)

    elif current>=3 and current-target>=3:
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
