import socket
import threading
import pickle
import time
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
# Initial servo angles are based on initial positions
motor_cmd = [105, 120, 95, 105, 105, 85, 90, 78]
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
                print("Robot states: ", robot_states)
            time.sleep(0.015)

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
            time.sleep(0.015)

        except Exception as e:
            print("Exception in send: {}".format(e))
            break


def run_hardcoded_gait():
    # New code for leg movement using Sine waves
    time_ax1 = np.arange(0, 2 * np.pi, 0.1)
    time_ax2 = np.arange(0 + np.pi, 2 * np.pi + np.pi, 0.1)
    amplitude1 = (20 * np.sin(time_ax1)).astype(int) + 105
    amplitude3 = (20 * np.sin(time_ax2)).astype(int) + 95

    amplitude5 = (20 * np.sin(time_ax2)).astype(int) + 80
    amplitude7 = (20 * np.sin(time_ax1)).astype(int) + 90

    amplitude2 = []
    amplitude4 = []
    amplitude6 = []
    amplitude8 = []

    for i in range(time_ax1.shape[0]):
        t = time_ax1[i]
        if t < np.pi / 2 or t > 3 * np.pi / 2:
            amplitude2.append(120)
            amplitude8.append(78)

            amplitude4.append(65)
            amplitude6.append(120)
        else:
            amplitude2.append(80)
            amplitude8.append(118)

            amplitude4.append(105)
            amplitude6.append(80)

    with lock:
        global motor_cmd
        motor_cmd_send = pickle.dumps(motor_cmd)
        client.send(motor_cmd_send)
    time.sleep(1.5)

    while True:
        for i in range(time_ax1.shape[0]):
            with lock:
                motor_cmd = [int(amplitude1[i]), amplitude2[i], int(amplitude3[i]), amplitude4[i],
                             180 - int(amplitude5[i]), amplitude6[i], 180 - int(amplitude7[i]), amplitude8[i]]
                print("Motor command: ", motor_cmd)
                motor_cmd_send = pickle.dumps(motor_cmd)
                client.send(motor_cmd_send)

            time.sleep(0.015)


def run_RL_algorithm():
    # This function uses robot_states and writes into motor_cmd
    while True:
        with lock:
            global motor_cmd
            # Write into motor_cmd here
        time.sleep(0.015)


# Create two threads to run send and receive in parallel
receive_thread = threading.Thread(target=receive, args=())
send_thread = threading.Thread(target=send, args=())


# send_thread.start()
send_thread.join()
time.sleep(1)
receive_thread.start()
run_RL_algorithm()
