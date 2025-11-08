#include <Servo.h>

#define TRIG 9
#define ECHO 10
#define SERVO_PIN 3

Servo doorServo;

void setup() {
  Serial.begin(9600);
  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);
  doorServo.attach(SERVO_PIN);
  doorServo.write(0);  // Door closed position
  Serial.println("Smart Door System Initialized");
}

void loop() {
  long duration;
  int distance;

  // Send ultrasonic pulse
  digitalWrite(TRIG, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG, LOW);

  // Read echo
  duration = pulseIn(ECHO, HIGH);
  distance = duration * 0.034 / 2; // Convert to cm

  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");

  // If person detected within 20 cm
  if (distance > 0 && distance < 20) {
    Serial.println("Person detected! Opening door...");
    doorServo.write(90); // Open door
    delay(3000);         // Keep door open for 3 seconds
    Serial.println("Closing door...");
    doorServo.write(0);  // Close door
  }

  delay(500);
}
