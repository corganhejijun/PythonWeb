import serial
connected = False
port = 'COM4'
baud = 9600

ser = serial.Serial(port, baud, timeout=0)

while not connected:
    #serin = ser.read()
    connected = True

    while True:
        reading = ser.readline()
        if len(reading) > 0:
            print reading
