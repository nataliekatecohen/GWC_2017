#include <Servo.h>

Servo servoLeft, servoRight;
const int buzzer = 6;

void setup() {
  // put your setup code here, to run once:
  servoLeft.attach(13);
  servoRight.attach(12);
  pinMode(buzzer, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  
  servoLeft.writeMicroseconds(10000);
  servoRight.writeMicroseconds(10000);
  delay(1000);
  
  servoLeft.writeMicroseconds(500);         // Left wheel counterclockwise
  servoRight.writeMicroseconds(-500);        // Right wheel clockwise
  delay(2000);

  servoLeft.writeMicroseconds(-500);         // Left wheel counterclockwise
  servoRight.writeMicroseconds(500);        // Right wheel clockwise
  delay(2000);

  tone(buzzer,1000);
  delay(1000);
  noTone(buzzer);
  delay(1000);
  }


