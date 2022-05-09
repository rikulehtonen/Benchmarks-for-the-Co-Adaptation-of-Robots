import socket
import threading
import pickle
from smbus import SMBus
import numpy as np
import time
import traceback

# Load the accelerometer and velocity module
from i2c_accelerometer import get_accelerometer_readings
#from pmw3901 import get_velocity_readings


addr = 0x10 # bus address
bus = SMBus(1)

# Replace it with the IP of the host computer, use a hotspot etc to connect both device to same network
# Not using UDP as of now
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('10.100.26.70', 5050))


def send_instructions_to_teensy(motor_cmd):
    # motor_cmd is a list of size 8
    ack = bus.write_i2c_block_data(addr, 0, motor_cmd)


def fetch_states_from_teensy():
    teensy_states = bus.read_i2c_block_data(addr, 0)
    teensy_states = [int(byte) for byte in teensy_states if byte]

    return teensy_states


# Receiving messages from Host computer
def receive():
    connected = True
    while connected:
        try:
            message = client.recv(1024)
            teensy_message = pickle.loads(message)
            print(teensy_message)
            send_instructions_to_teensy(teensy_message)
            time.sleep(0.2)

        except Exception as e:
            # close connection when error
            print("An error occured in receive!: {}".format(traceback.print_exc()))
            #client.close()
            continue


# sending messages to Host computer
def send():
    connected = True
    while connected:
        try:
            teensy_states = fetch_states_from_teensy()
            acc_vector = get_accelerometer_readings()
            #vec_vector = get_velocity_readings()

            #teensy_states = np.concatenate((teensy_states, acc_vector, vec_vector))
            teensy_states.extend(acc_vector)
            print(teensy_states)
            #teensy_states = np.concatenate((teensy_states, acc_vector))
            teensy_states = pickle.dumps(teensy_states)
            client.send(teensy_states)
            time.sleep(0.2)

        except Exception as e:
            print("An error occured in send!: {}".format(traceback.print_exc()))
            #client.close()
            continue


# Create two threads to run send and receive in parallel
receive_thread = threading.Thread(target=receive, args=())
send_thread = threading.Thread(target=send, args=())

receive_thread.start()
#receive_thread.join()
time.sleep(1)


send_thread.start()

