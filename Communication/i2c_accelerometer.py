import time
import board
import busio
import adafruit_adxl34x
import numpy as np


i2c = busio.I2C(board.SCL, board.SDA)
time.sleep(2)
accelerometer = adafruit_adxl34x.ADXL345(i2c)


def get_accelerometer_readings():
    x_acc, y_acc, z_acc = accelerometer.acceleration
    return np.array([x_acc, y_acc, z_acc])

