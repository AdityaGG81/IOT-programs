#include <Servo.h>

Servo myservo;   // create servo object

int servoPin = 9;  // Servo signal pin connected to D9
int pos = 0;       // variable to store servo position

void setup() {
  myservo.attach(servoPin);  // attach servo to pin
}

void loop() {
  // Sweep from 0° to 180°
  for (pos = 0; pos <= 180; pos += 1) {
    myservo.write(pos);      // move servo to position
    delay(15);               // small delay for smooth movement
  }

  // Sweep back from 180° to 0°
  for (pos = 180; pos >= 0; pos -= 1) {
    myservo.write(pos);
    delay(15);
  }
}
