import socket
import threading
import time

# connection data
host = "127.0.0.1"
port = 5050

# starting server
# socket.SOCK_DGRAM = UDP

# TCP connection
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()


def handle(client):
  
  client.send('Connected to server!'.encode('ascii'))

  connected = True
  while connected:
    message = client.recv(1024)
    data = message.decode('ascii')
    print(data+'\n')
    msg = input("enter text : ")
    print('\n')
    
    client.send(msg.encode('ascii'))

# listening function
def receive():
    while True:
        # accept connection
        client, address = server.accept()
        print("Connected with {}".format(str(address)))

        # start handling thread for client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()
