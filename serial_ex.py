import serial
import sys
import time

# Get a serial port from the command line argument. Ex: serial_ex.py COM4
PORT = sys.argv[1]

try:
    ser = serial.Serial(
        port=PORT,
        baudrate=115200,
        parity=serial.PARITY_NONE,
        bytesize=serial.EIGHTBITS,
        timeout=10,
        stopbits=serial.STOPBITS_ONE,
        write_timeout=4)

except ValueError:
    print("\nParameter are out of range, e.g. baud rate ...")
    sys.exit(1)

except serial.SerialException:
    print("\nDevice can not be found or can not be configured."
          "\nCheck the PORT number")

# Enter a command or write data to the serial interface

# 'cp1252' is an encoding. Try 'utf-8' encoding format if this doesn't work.
# Convert the data into bytes before sending it.
data = bytes("Device_Info\n", 'cp1252')
ser.write(data)
# Add 2 seconds time delay so that data gets collected in the buffer
time.sleep(2)

# Read output data

output = b''                     # empty output variable of type (bytes)
while ser.in_waiting:            # While output data present in the buffer
    output += ser.read(1024)     # Append 1024 bytes of data in output

# Decode the data back into the (ASCII)string format
output = output.decode('cp1252')
print(output)                    # Print final output

ser.close()                      # Close the connection
