Install Raspberry Pi OS. It might work with other OS as well, but not tested.
Make sure Python 3 is installed.

Install following python libraries:
```
pip install smbus
sudo pip install adafruit-adxl345
sudo pip install pmw3901
```
Checkout
<a href="https://github.com/adafruit/Adafruit_Python_ADXL345" target="_blank">Adafruit</a>
<a href="https://github.com/pimoroni/pmw3901-python" target="_blank">PMW3901</a>

Run the python script as below. Make sure that the Host Node is already up and running.
```
python Raspberry_node.py
```