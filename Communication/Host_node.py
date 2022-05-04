import socket
import threading
import pickle
import numpy as np


# Replace it with the local IP of Host machine
host = "127.0.0.1"
port = 5050


# TCP connection
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

# Connect to Raspberry Pi Client
client, address = server.accept()


# Create global variables
motor_cmd = np.zeros(8)
# 8 motor states, 3 acceleration, 2 velocity
robot_states = np.zeros(13)

lock = threading.Lock()


# Receive values from Raspberry Pi
def receive():
    connected = True
    while connected:
        message = client.recv(1024)
        robot_states_nw = pickle.loads(message)
        with lock:
            global robot_states
            robot_states = robot_states_nw


# Send values to Raspberry Pi
def send():
    with lock:
        client.send(motor_cmd)


def run_RL_algorithm():
    # This function uses robot_states and writes into motor_cmd
    return


# Create two threads to run send and receive in parallel
receive_thread = threading.Thread(target=receive, args=())
send_thread = threading.Thread(target=send, args=())

receive_thread.start()
send_thread.start()

run_RL_algorithm()
