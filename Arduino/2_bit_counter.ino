int pins[] = {8, 9};  // LEDs on pins 8 and 9

void setup() {
  for (int i = 0; i < 2; i++) {
    pinMode(pins[i], OUTPUT);
  }
}

void loop() {
  for (int i = 0; i < 4; i++) {   // 00 → 11
    digitalWrite(pins[0], bitRead(i, 0));
    digitalWrite(pins[1], bitRead(i, 1));
    delay(1000);
  }
}
