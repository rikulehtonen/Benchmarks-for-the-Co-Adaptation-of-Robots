import socket
import threading
import numpy as np
import pickle


host_rl = socket.gethostbyname("LAPTOP-I2AD52B7")
host_rl = "10.100.0.118"
port_rl = 5050


# TCP client on Raspberry Pi side
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host_rl, port_rl))



def send_instructions_to_teensy(message):
    pass

# Recieve message from Host computer
def receive_tcp(client):
    try:
        while True:
            message = client.recv(1024)
            teensy_message = pickle.loads(message)
            # TODO send instructions to the Teensy
            send_instructions_to_teensy(teensy_message)


    except Exception as e:
        # close connection when error
        print("An error occured!")
        print(e)
        client.close()




# UDP server on Raspberry Pi side
print("here")
host_raspi = "192.168.137.118"
port_raspi = 5060
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((host_raspi, port_raspi))

byte_address_pair = server.recvfrom(1024)
print(byte_address_pair)
message = byte_address_pair[0]
address = byte_address_pair[1]
print(address)
msg = "Hello from UDP server"
msg = str.encode(msg)
server.sendto(msg, address)

#receive_tcp(client)




