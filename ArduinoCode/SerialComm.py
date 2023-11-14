import serial
import time

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
while True: 
	if(alt == True):	
		try:
			arduino.write("Counter".encode())
			data = arduino.readline()
			if data:
				print(data)
				alt = True
			time.sleep(5)
		except Exception as e:
			print(e)
			arduino.close()

	if(alt == False):	
		try:
			arduino.write("Count".encode())
			data = arduino.readline()
			if data:
				print(data)
				alt = False
			time.sleep(5)
		except Exception as e:
			print(e)
			arduino.close()

	#time.sleep(5)