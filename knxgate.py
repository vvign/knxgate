#!/usr/bin/python3
import serial
import sys
import time


line1 =  str(sys.argv[1])
cmd =  str(sys.argv[2])
actuator =  str(sys.argv[3])

#DEBUG ARGUMENT
#print "line:" + line1
#print "actuator:" + actuator
#print "command:" + cmd

ll = "@D" + line1
scr = "@w" + cmd + actuator
#print(""+ll)
#print(""+scr)

data1 = "@D" +line1
res = bytes(data1, 'utf-8')

print(res)
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
ser.write(res)
ser.close()

time.sleep(0.2)

data2 = "@w" + cmd + actuator
res2 = bytes(data2, 'utf-8')
print(res2)
ser2 = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
ser2.write(res2)
ser2.close()
