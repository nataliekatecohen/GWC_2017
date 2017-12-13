// int sensor = ;

#include <Servo.h>  
Servo servoLeft;
Servo servoRight;
int readNum;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode (A3, INPUT);
  servoLeft.attach(13);
  servoRight.attach(12);
}

void loop() {
  // put your main code0 here, to run repeatedly:
readNum = digitalRead(A3);
if (readNum == 0){
  servoLeft.writeMicroseconds(2000);
  servoRight.writeMicroseconds(-2000);
}
if (readNum == 1) {
  servoLeft.writeMicroseconds(500);
  servoRight.writeMicroseconds(-10000);
 }
}

