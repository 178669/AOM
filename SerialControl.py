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
    file = open("ArduinoCode/LastIndex.txt", "r")
    current = int(file.read())#ra
    file.close()

    file = open("ArduinoCode/LastIndex.txt", "w")
    save = str(target)
    file.write(save)#update page
    CW=2
    if (abs(current - target) > 3) and current>3:
        CW = 0
        dis = abs(abs(current - max) - target)
        return (CW, dis)
    elif (abs(current - target) > 3) and current<=3:
        CW = 1
        dis = abs(abs(current - max) - target)
        return (CW, dis)
    else:
        CW = 1
        dis = target - current
        return (CW, dis)
    '''
    if abs(abs(current - max) - target) < abs(target - current):
        CW = 1
        return (CW, abs(abs(current - max) - target))
    else:
        CW = 0
        return (CW, abs(target-current));
    '''
