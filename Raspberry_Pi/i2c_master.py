#  Raspberry Pi Master for Arduino Slave
#  i2c_master_pi.py
#  Connects to Arduino via I2C
#  DroneBot Workshop 2019
#  https://dronebotworkshop.com

from smbus import SMBus
import time

addr = 0x10 # bus address
bus = SMBus(1) # indicates /dev/ic2-1
time.sleep(1)
numb = 1

print ("Enter 1 for ON or 0 for OFF")

while numb == 1:

	ledstate = input(">>>>   ")
                       
	if ledstate == "0":
		bus.write_byte_data(addr, 180, 0) # switch it on
		# time.sleep(1)
		# bus.write_byte(addr, 180)
	elif ledstate == "1":
		bus.write_byte_data(addr, 0, 180) # switch it on
	elif ledstate == "2":
		value = bus.read_i2c_block_data(addr, 0)
		value = ("".join([chr(byte) for byte in value if byte]))
		print(value)
	elif ledstate == "3":
		value = bus.read_byte_data(addr, 0x02) #
		print(value)
	elif ledstate == "4":
		value = bus.read_byte(addr) #
		print(chr(value))

	elif ledstate == "5":
		value = bus.write_i2c_block_data(addr, 0, [180, 90, 0])

	else:
		numb = 0