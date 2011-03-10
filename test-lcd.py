import serial
import time

lcd = serial.Serial("/dev/ttyACM0", 9600)
time.sleep(1.5)
lcd.write('test')
