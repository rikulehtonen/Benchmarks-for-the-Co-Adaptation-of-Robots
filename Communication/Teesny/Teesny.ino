#include <i2c_driver_Wire.h>
#include <Servo.h>
#include <sstream>
using namespace std;


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
  Wire1.read()
  
  byte rxbyte;
  int motor_cmd[8];
  idx = 0
  
  # Read next 8 values
  while (Wire1.available()) {
    rxbyte = Wire1.read();
    Serial.println("Data received:");
    Serial.println(rxbyte);
    motor_cmd[idx] = rxbyte;
  }

  for (int idx; idx < 8; idx++) {
    switch (idx) {
      case 0:
      Servo1.write(motor_cmd[idx]);

      case 1:
      Servo2.write(motor_cmd[idx]);

      case 2:
      Servo3.write(motor_cmd[idx]);

      case 3:
      Servo4.write(motor_cmd[idx]);

      case 4:
      Servo5.write(motor_cmd[idx]);

      case 5:
      Servo6.write(motor_cmd[idx]);

      case 6:
      Servo7.write(motor_cmd[idx]);

      case 7:
      Servo8.write(motor_cmd[idx]);
    }
  }
}

void requestEvent() {
 Serial.println("Inside Request");
 Wire1.write(Servo1.read()); 
 Wire1.write(Servo2.read());
 Wire1.write(Servo3.read());
 Wire1.write(Servo4.read());
 Wire1.write(Servo5.read());
 Wire1.write(Servo6.read());
 Wire1.write(Servo7.read());
 Wire1.write(Servo8.read());
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
