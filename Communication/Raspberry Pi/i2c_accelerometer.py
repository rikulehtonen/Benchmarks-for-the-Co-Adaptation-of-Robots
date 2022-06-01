import time
import board
import busio
import adafruit_adxl34x
from threading import Thread, Lock


i2c = busio.I2C(board.SCL, board.SDA)
time.sleep(2)
accelerometer = adafruit_adxl34x.ADXL345(i2c)

acc_states = [0, 0, 0]
lock = Lock()


def update_accelerometer_readings():
    while True:
        try:
            x_acc, y_acc, z_acc = accelerometer.acceleration
            with lock:
                global acc_states
                acc_states = [round(x_acc, 3), round(y_acc, 3), round(z_acc, 3)]

        except Exception as e:
            time.sleep(0.015)


def get_accelerometer_readings():
    with lock:
        global acc_states
        return acc_states


acc_thread = Thread(target=update_accelerometer_readings, args=())
acc_thread.start()


if __name__ == "__main__":
    print(get_accelerometer_readings())

