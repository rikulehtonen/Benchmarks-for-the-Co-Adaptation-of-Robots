#/usr/bin/env python
import time
from pmw3901 import PMW3901, BG_CS_FRONT_BCM, BG_CS_BACK_BCM
import numpy as np
from threading import Thread, Lock

'''
parser = argparse.ArgumentParser()
parser.add_argument('--board', type=str,
                    choices=['pmw3901', 'paa5100'],
                    required=True,
                    help='Breakout type.')
parser.add_argument('--rotation', type=int,
                    default=0, choices=[0, 90, 180, 270],
                    help='Rotation of sensor in degrees.')
parser.add_argument('--spi-slot', type=str,
                    default='front', choices=['front', 'back'],
                    help='Breakout Garden SPI slot.')

args = parser.parse_args()
'''

args = {
    'board': 'pmw3901',
    'rotation': 0,
    'spi_slot': 'back'
}

# Pick the right class for the specified breakout
SensorClass = PMW3901 if args["board"] == 'pmw3901' else None

flo = SensorClass(spi_port=0, spi_cs=1, spi_cs_gpio=BG_CS_FRONT_BCM if args["spi_slot"] == 'front' else BG_CS_BACK_BCM)
flo.set_rotation(args["rotation"])


velocity_states = [0, 0]
lock = Lock()

def update_velocity_readings():
    tx = 0
    ty = 0

    try:
        while True:
            try:
                x, y = flo.get_motion()
            except RuntimeError:
                print("Exception in Velocity Sensor!!!")
                continue
            tx += x
            ty += y
            print("Relative: x {:03d} y {:03d} | Absolute: x {:03d} y {:03d}".format(x, y, tx, ty))
            with lock:
                global velocity_states
                velocity_states = [x, y]

            time.sleep(0.1)

    except Exception as e:
        print(e)


def get_velocity_readings():
    with lock:
        return velocity_states


velocity_thread = Thread(target=update_velocity_readings, args=())
velocity_thread.start()


if __name__ == "__main__":
    while True:
        print(get_velocity_readings())
        time.sleep(1)