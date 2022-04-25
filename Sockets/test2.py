import socket
import threading
import time
import os


# connecting to server
# connection data
host_raspi = "127.0.0.1"
port_raspi = 5060

# TCP client on Raspberry Pi side
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.connect((host_raspi, port_raspi))

message = client.recv(1024).decode('ascii')
print(message)
print("here")
client.send('I am sending back'.encode('ascii'))