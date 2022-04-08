#  Raspberry Pi Master for Arduino Slave
#  i2c_master_pi.py
#  Connects to Arduino via I2C
  
#  DroneBot Workshop 2019
#  https://dronebotworkshop.com

from smbus import SMBus
import time

addr = 0x8 # bus address
bus = SMBus(1) # indicates /dev/ic2-1
time.sleep(1)
numb = 1

print ("Enter 1 for ON or 0 for OFF")
while numb == 1:

	ledstate = input(">>>>   ")

	if ledstate == "1":
		bus.write_byte(addr, 0x1) # switch it on
	elif ledstate == "0":
		bus.write_byte(addr, 0x0) # switch it on
	elif ledstate == "2":
		bus.read_i2c_block_data(addr,1)
	else:
		numb = 0
