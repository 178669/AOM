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
items = [1, 2, 3, 4, 5, 6]
#fucntion to determine if CW or CCW is faster
def calc(filepath, target, max):
    file = open(filepath, "r")
    current = f.read()
    
    if (current == 5 && target == 1):
        CW = true
        return 1

    elif (current == 6 && target == 1)||(current == 6 && target ==2):
        CW = true
        return target

    
    if max - current >= 3:
        CW = true
        return max - current




def 