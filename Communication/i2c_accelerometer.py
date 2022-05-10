import time
import board
import busio
import adafruit_adxl34x
import numpy as np


i2c = busio.I2C(board.SCL, board.SDA)
time.sleep(2)
accelerometer = adafruit_adxl34x.ADXL345(i2c)


def get_accelerometer_readings():
    for _ in range(30):
        try:
            x_acc, y_acc, z_acc = accelerometer.acceleration
            return [round(x_acc, 3), round(y_acc, 3), round(z_acc, 3)]
        except Exception as e:
            #print("Exception in accelerometer: {}".format(e))
            time.sleep(0.05)
            pass
    return [0, 0 ,0]


if __name__ == "__main__":
    print(get_accelerometer_readings())

