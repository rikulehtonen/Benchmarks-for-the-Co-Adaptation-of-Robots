import socket
import threading
import time

# connection data
host_raspi = "127.0.0.1"
port_raspi = 5050

host_rl = socket.gethostbyname("LAPTOP-I2AD52B7")
port_rl = 5060


# UDP Server on Raspberry Pi side
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((host_raspi, port_raspi))
server.listen()

# TCP client on Raspberry Pi side
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host_rl, port_rl))


# Handle request for UDP clients
def handle_udp_requests(udp_client):
  
  udp_client.send('Connected to server!'.encode('ascii'))
  connected = True
  while connected:
    message = udp_client.recv(1024)
    data = message.decode('ascii')
    print(data+'\n')
    msg = input("enter text : ")
    print('\n')
    udp_client.send(msg.encode('ascii'))


# listening function for UDP server
def accept_udp():
    while True:
        # accept connection
        udp_client, address = server.accept()
        print("Connected with {}".format(str(address)))

        # start handling thread for client
        thread = threading.Thread(target=handle_udp_requests, args=(udp_client,))
        thread.start()

def receive_tcp():
    connected = True
    while connected:
        print("\n")
        try:
            
            message = client.recv(1024).decode('ascii')
            print(message)
            print('\n')
        except:
            # close connection when error
            print("An error occured!")
            client.close()
            break



