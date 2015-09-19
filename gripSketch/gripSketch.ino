#include <Servo.h>

Servo servoOne;
Servo servoTwo;
Servo servoThree;

boolean opened = true;

void setup() {
  Serial.begin(9600);
  servoOne.attach(7);
  servoTwo.attach(8);
  servoThree.attach(9);
  openServos();
}

void loop() {
  serialEvent();
}

void serialEvent() {
  int readValue = Serial.read();
  Serial.println(readValue);
  if (readValue==1){
    toggle();
  } else {
    digitalWrite(13,LOW);
  }
}

void toggle(){
  if (opened == true){
    closeServos();
    opened = false;
  } else {
    openServos();
    opened = true;
  }
}

void closeServos(){
  servoOne.write(25);
  servoTwo.write(25);
  servoThree.write(25);
}

void openServos(){
  servoOne.write(0);
  servoTwo.write(0);
  servoThree.write(0);
}

