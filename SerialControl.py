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
        arduino.write("Counter".encode())
        data = arduino.readline()
        if data:
            print(data)
            alt = True
        time.sleep(5)
        controller.show_frame(StartPage)
    except Exception as e:
        print(e)
        arduino.close()

def calc():

def 