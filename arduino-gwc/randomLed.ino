int led = 13;
int led2 = 12;
int led3 = 11;

void setup() {
  // put your setup code here, to run once:
pinMode(led, OUTPUT);
pinMode(led2, OUTPUT);
pinMode(led3, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
int randomLed = 11 + rand() % 3;
digitalWrite(randomLed, HIGH);
delay(1000);
digitalWrite(randomLed, LOW);
delay(1000);
}

