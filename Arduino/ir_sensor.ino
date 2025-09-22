int irPin = 9;        // IR sensor output
int ledPin = 13;      // LED or buzzer pin

void setup() {
  pinMode(irPin, INPUT);
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int val = digitalRead(irPin);

  if (val == LOW) {  // obstacle detected
    digitalWrite(ledPin, HIGH);
    Serial.println("Obstacle detected");
  } else {
    digitalWrite(ledPin, LOW);
    Serial.println("No obstacle");
  }

  delay(200);
}
