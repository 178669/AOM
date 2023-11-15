from tkinter import *
import tkinter as tk
import time
import serial
#from test import StartPage
def controlmotor():
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
    try:
        arduino.write("Counter3".encode())
        data = arduino.readline()
        if data:
            print(data)
            alt = True
        time.sleep(5)
        controller.show_frame(StartPage)
    except Exception as e:
        print(e)
        arduino.close()
#function to determine if CW or CCW is faster
#assuming CW is associated with positive positional indicies
def calc(filepath, target, max):
    file = open(filepath, "r")
    current = f.read()
    CW=2
    if abs(current - max - target) < abs(target - current):
        CW = 1
        return (CW, abs(current - max - target))
    else:
        CW = 0
        return (CW, abs(target-current));

