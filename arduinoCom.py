import serial
import time
print("this module has started")
ser=serial.Serial(port='/dev/ttyACM0',baudrate=9600)
time.sleep(2)
print(ser.readline())
sender=True
#read=ser.readline()
#print(read)
while(sender):
	y=raw_input("input a value: ")
	if(y=='1' or y=='0'):
	    ser.write(y)
	else:
	    sender=False
	


