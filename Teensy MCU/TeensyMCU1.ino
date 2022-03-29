#include Servo.h
#include Wire.h

Servo servo1; //Front left shoulder
Servo servo2; //Front left knee
Servo servo3; //Front right shoulder
Servo servo4; //Front right knee
Servo servo5; //Rear left shoulder
Servo servo6; //Rear left knee
Servo servo7; //Rear right shoulder
Servo servo8; //Rear right knee

void setup() {
  // put your setup code here, to run once:
  servo1.attach(2);
  servo2.attach(3);
  servo3.attach(4);
  servo4.attach(5);
  servo5.attach(6);
  servo6.attach(7);
  servo7.attach(8);
  servo8.attach(9);
  // set servos to mid-point angle
  servo1.write(90);
  servo2.write(90);
  servo3.write(90);
  servo4.write(90);
  servo5.write(90);
  servo6.write(90);
  servo7.write(90);
  servo8.write(90);
  Wire.begin(); // join I2C bus
  Wire.onReceive(receiveEvent); // when the Teensy receives commands, the event is triggered
  Wire.onRequest(requestEvent); //when Teensy is requested to report angles to the Raspberry Pi 
  Serial.begin(9600); //start serial comms
}

void loop() {
  // put your main code here, to run repeatedly:
  delay(10);
}

void receiveEvent(int howMany)  {   //howMany = how many bytes of data to receive. This case 8. 1 for each servo
  // save the commands into integers
  int angle1 = Wire.read();
  int angle2 = Wire.read();
  int angle3 = Wire.read();
  int angle4 = Wire.read();
  int angle5 = Wire.read();
  int angle6 = Wire.read();
  int angle7 = Wire.read();
  int angle8 = Wire.read();
  // write the angles to the servos
  servo1.write(angle1);
  servo3.write(angle3);
  servo5.write(angle5);
  servo7.write(angle7);
  servo2.write(angle2);
  servo4.write(angle4);
  servo6.write(angle6);
  servo8.write(angle8);
  }
}

void requestEvent() {
  Wire.write(servo1.read());
  Wire.write(servo2.read());
  Wire.write(servo3.read());
  Wire.write(servo4.read());
  Wire.write(servo5.read());
  Wire.write(servo6.read());
  Wire.write(servo7.read());
  Wire.write(servo8.read());
}
