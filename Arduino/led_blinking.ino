int ledPin = 13;  // built-in LED on Arduino

void setup() {
  pinMode(ledPin, OUTPUT);
}

void loop() {
  digitalWrite(ledPin, HIGH); // LED ON
  delay(1000);
  digitalWrite(ledPin, LOW);  // LED OFF
  delay(1000);
}
