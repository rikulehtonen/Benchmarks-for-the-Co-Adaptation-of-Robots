Install Arduino app and <a href="https://www.pjrc.com/teensy/teensyduino.html" target="_blank">Teensyduino </a> (Software add-on for Arduino).

I2C Slave mode is not supported for Teensy 4.0 by the current version of Wire library.
Instead, include <i2c_driver_Wire.h> library in Arduino libraries.