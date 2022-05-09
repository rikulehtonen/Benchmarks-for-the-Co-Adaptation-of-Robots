#include <Arduino.h>
#include <i2c_driver.h>
#include <i2c_driver_Wire.h>
#include <Servo.h>
#include <sstream>
using namespace std;

int count = 0;
Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;
Servo servo5;
Servo servo6;
Servo servo7;
Servo servo8;

void receiveEvent(int howMany)
{
  Serial.println("Inside Receive");

  // Ignore first value as it is the address of the register
  Wire1.read();

  byte rxbyte;
  int motor_cmd[9];
  int idx = 0;
  int true_request = 0;

  // Read next 8 values
  while (Wire1.available()) {
    rxbyte = Wire1.read();
    Serial.println("Data received:");
    Serial.println(rxbyte);
    motor_cmd[idx] = int(rxbyte);
    idx = idx + 1;
    if (idx == 7) {
      true_request = 1;
    }
  }

  if (true_request == 1) {
    Serial.println("Size of array:");
    Serial.println(sizeof(motor_cmd));
    for (int i = 0; i < 8; i++) {
      Serial.println(motor_cmd[i]);
    }
  }



  if (true_request == 1) {
    for (int idx = 0; idx < 8; idx++) {
      Serial.println("To switch");
      switch (idx) {
        case 0:
          servo1.write(motor_cmd[idx]);

        case 1:
          servo2.write(motor_cmd[idx]);

        case 2:
          servo3.write(motor_cmd[idx]);

        case 3:
          servo4.write(motor_cmd[idx]);

        case 4:
          servo5.write(motor_cmd[idx]);

        case 5:
          servo6.write(motor_cmd[idx]);

        case 6:
          servo7.write(motor_cmd[idx]);

        case 7:
          servo8.write(motor_cmd[idx]);
      }
    }
  }
}

void requestEvent() {
  Serial.println("Inside Request");
  Serial.println(servo1.read());
  Serial.println(servo2.read());
  Serial.println(servo3.read());
  Serial.println("----------\n");
  Wire1.write(servo1.read());
  Wire1.write(servo2.read());
  Wire1.write(servo3.read());
  Wire1.write(servo4.read());
  Wire1.write(servo5.read());
  Wire1.write(servo6.read());
  Wire1.write(servo7.read());
  Wire1.write(servo8.read());
}

void setup() {
  // put your setup code here, to run once:
  Wire1.begin(0x10);                // join i2c bus with address #9
  Wire1.onReceive(receiveEvent); // register event
  Wire1.onRequest(requestEvent);
  Serial.begin(9600);           // start serial for output
  servo1.attach(2);              // consequent servos to be attache from 4-->
  servo2.attach(3);
  servo3.attach(4);              // consequent servos to be attache from 4-->
  servo4.attach(5);
  servo5.attach(6);              // consequent servos to be attache from 4-->
  servo6.attach(7);
  servo7.attach(8);              // consequent servos to be attache from 4-->
  servo8.attach(9);

}

void loop() {
  // put your main code here, to run repeatedly:
  delay(10);
  count++;

}