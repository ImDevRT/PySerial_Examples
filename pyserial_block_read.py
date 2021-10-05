import sys
import time
import serial

# Get a serial port from the command line argument
if len(sys.argv != 2):
    print("Please enter a valid serial port\n"
          "Ex: python pyserial_block_read.py COM5")
    sys.exit(1)

PORT = sys.argv[1].upper()

try:
    ser_con = serial.Serial(
              port=PORT,
              baudrate=115200,
              parity=serial.PARITY_NONE,
              bytesize=serial.EIGHTBITS,
              timeout=10,
              stopbits=serial.STOPBITS_ONE,
              write_timeout=4)

except ValueError:
    print("\nParameter are out of range, e.g. baud rate ...")

except serial.SerialException:
    print("\nDevice can not be found or can not be configured."
          "\nCheck the PORT number")

# Transmit data to the receiving UART
data = bytes("help\n", "utf-8")
ser_con.write(data)

# Read output data
output_data = ""
while True:
    output_data += ser_con.read(1).decode("utf-8")
    if (output_data == ""):
        break
    time.sleep(0.1)

print(output_data)
