import socket
import threading
import pickle
import time
import random

import numpy as np


# Replace it with the local IP of Host machine
# host = "10.100.26.70"
host = "169.254.64.94"
port = 5050


# TCP connection
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

# Connect to Raspberry Pi Client
client, address = server.accept()


# Create global variables
motor_cmd = [120, 110, 100, 90, 80, 70, 60, 50]
# 8 motor states, 3 acceleration, 2 velocity
robot_states = [0]*13

lock = threading.Lock()


# Receive values from Raspberry Pi
def receive():
    connected = True
    while connected:
        try:
            message = client.recv(1024)
            robot_states_nw = pickle.loads(message)
            with lock:
                global robot_states
                robot_states = robot_states_nw
                print(robot_states)
            time.sleep(0.2)

        except Exception as e:
            print("Exception in receive: {}".format(e))
            break


# Send values to Raspberry Pi
def send():
    connected = True
    while connected:
        try:
            with lock:
                global motor_cmd
                # motor_cmd = [val-2 for val in motor_cmd]
                motor_cmd_send = pickle.dumps(motor_cmd)
                client.send(motor_cmd_send)
            time.sleep(0.2)

        except Exception as e:
            print("Exception in send: {}".format(e))
            break


def run_RL_algorithm():
    # This function uses robot_states and writes into motor_cmd
    while True:
        with lock:
            global motor_cmd
            motor_cmd = [x-2 for x in motor_cmd]
        time.sleep(2)


# Create two threads to run send and receive in parallel
receive_thread = threading.Thread(target=receive, args=())
send_thread = threading.Thread(target=send, args=())


send_thread.start()
#send_thread.join()
time.sleep(1)

receive_thread.start()
run_RL_algorithm()
