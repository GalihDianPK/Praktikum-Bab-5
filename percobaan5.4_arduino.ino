#include <Servo.h>

Servo myServo;
int angle = 90;

void setup() {
  myServo.attach(2);  // Sesuaikan pin servo
  myServo.write(angle);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    angle = Serial.read();
    angle = constrain(angle, 0, 180);

    // Membalik arah pergerakan servo
    int reversedAngle = 180 - angle;
    myServo.write(reversedAngle);
  }
}
