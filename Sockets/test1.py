import socket
import threading
import time
import os



# connecting to server
# connection data
host_raspi = "127.0.0.1"
port_raspi = 5050


# UDP Server on Raspberry Pi side
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((host_raspi, port_raspi))
#server.listen()


	
server.sendto('Sending from UDP socket'.encode('ascii'), ("127.0.0.1", 5060))



udp_client, address = server.accept()
print("Connected with {}".format(str(address)))
udp_client.send('Connected to server!'.encode('ascii'))
while True:
    pass
    #print(udp_client)
