# Python ArduSiPM Serial Interface With Graphing Utilities
# Authors Riccardo Iacob, Mattia Zanovello
# Date 15/06/2022

import sys
import time
import csv
import serial
import serial.tools.list_ports
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Find available serial ports
# If none are available, exit
print("Scanning available serial ports...")
# List the available serial ports
serialPorts = list(serial.tools.list_ports.comports())
# If the serialPort list length is null, there are no serial ports available
if serialPorts.__len__() <= 0:
    print("No serial ports found! Exiting...")
    sys.exit()
print("Available serial ports:")
# Print available serial ports and look for ArduSiPM
# If available, connect to ArduSiPM
# If not available, exit
ser = serial.Serial()
# For each serialPort in the serialPorts list
for serialPort in serialPorts:
    # Print the serialPort
    print("- " + serialPort.description)
    # If the serialPort's description contains "Arduino", an ArduSiPM was possibly found
    # Attempt a connection
    if serialPort.description.find("Serial") > 0:
        print("ArduSiPM found on " + serialPort.name + ", attempting connection...")
        ser.baudrate = 115200
        ser.timeout = None
        ser.port = str(serialPort).split(" ")[0]
        ser.open()
        print("Connected to ArduSiPM on " + serialPort.name)
        break
    # If no ArduSiPM is found, exit
    else:
        print("No ArduSiPM found! Exiting...")
        sys.exit()
        break

# Print all lines incoming from serial
# This is just temporary
print("Beginning data reception...")
while 1:
    serStr = ser.readline().rstrip().decode("ascii")
    print("COUNTS: " + serStr.removeprefix("$"))


