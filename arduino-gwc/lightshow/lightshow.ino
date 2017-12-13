int led = 11, led2 = 12, led3 = 13;

void setup() {
  // put your setup code here, to run once:
  pinMode(led, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  for (int i = 11; i < 14; i++){
    digitalWrite(i, HIGH);
    delay(500);
    digitalWrite(i, LOW);
    delay(500);
  }
  for (int n = 13; n > 10; n--){
    digitalWrite(n, HIGH);
    delay(500);
    digitalWrite(n, LOW);
    delay(500);
  }
}
