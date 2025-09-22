int pins[] = {8, 9, 10};  // LEDs on pins 8, 9, 10

void setup() {
  for (int i = 0; i < 3; i++) {
    pinMode(pins[i], OUTPUT);
  }
}

void loop() {
  for (int i = 0; i < 8; i++) {   // 000 → 111
    digitalWrite(pins[0], bitRead(i, 0));
    digitalWrite(pins[1], bitRead(i, 1));
    digitalWrite(pins[2], bitRead(i, 2));
    delay(1000);
  }
}
