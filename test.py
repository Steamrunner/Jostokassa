import serial

SERIAL = 1
KEYBOARD = 2

mode = SERIAL
ser = serial.Serial("/dev/ttyS0", 9600)

def getInput():
	returnString = ""
	if mode == SERIAL:
		returnString = ser.readline()
		returnString = returnString.strip()
	elif mode == KEYBOARD:
		returnString = raw_input()
	else:
		print "Input missconfigured!!!"
	return returnString


while True:
	print getInput()
