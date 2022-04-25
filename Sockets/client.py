import socket
import threading
import time
import os



# connecting to server

host_name = "64-79-F0-CE-BD-0A"
host_name = "LAPTOP-I2AD52B7"
print(socket.gethostbyname(host_name))


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('10.100.0.118', 5050))


# listening to server and sending Nickname
def receive():
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

# sending messages to server
def write():
    connected = True
    while connected:
        message = input('enter message : ')
        print('\n')
        client.send(message.encode('ascii'))
        print('\n')
        

# starting threads for listening and writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
