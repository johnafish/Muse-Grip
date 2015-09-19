
void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
}

void loop() {
  serialEvent();
}

void serialEvent() {
  int readValue = Serial.read();
  Serial.println(readValue);
  if (readValue==1){
    blinker();
  } else {
    digitalWrite(13,LOW);
  }
}

void blinker(){
  for (int i=0;i<2;i++){
    digitalWrite(13, HIGH);
    delay(500);
    digitalWrite(13, LOW);
    delay(500);
  }
}

