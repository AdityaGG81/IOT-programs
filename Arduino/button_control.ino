// Button Control Program
// Read a button input and control an LED

int buttonPin = 2;   // Button connected to D2
int ledPin = 13;     // Built-in LED

void setup() {
  pinMode(buttonPin, INPUT);   // Set button as input
  pinMode(ledPin, OUTPUT);      // Set LED as output
  Serial.begin(9600);           // Start serial communication for debugging
}

void loop() {
  int buttonState = digitalRead(buttonPin);  // Read button state
  
  if (buttonState == HIGH) {
    digitalWrite(ledPin, HIGH);   // Turn LED ON when button pressed
    Serial.println("Button pressed - LED ON");
  } else {
    digitalWrite(ledPin, LOW);    // Turn LED OFF when button released
    Serial.println("Button released - LED OFF");
  }
  
  delay(50);  // Small delay to debounce
}
