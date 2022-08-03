import serial
#from escpos.constants import GS

def openSerialPort(port, baudrate = 9600, bytesize = serial.EIGHTBITS, parity = serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE, timeout = None, xonxoff = False, rtscts = False, dsrdtr = False):
    ser = serial.Serial()

    ser.port = port
    ser.baudrate = baudrate
    ser.bytesize = bytesize
    ser.parity = parity
    ser.stopbits = stopbits
    ser.timeout = timeout
    ser.xonxoff = xonxoff
    ser.rtscts = rtscts
    ser.dsrdtr = dsrdtr

    ser.open()
    return ser

ser = openSerialPort('COM5')

pass

#a = chr(0x0A)

for _ in range(5):
    ser.write(b'\x0A')  # UTF-8

ser.write(b'\x1D\x56\x00')


ser.close()
