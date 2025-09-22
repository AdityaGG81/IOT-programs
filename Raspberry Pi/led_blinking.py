import RPi.GPIO as GPIO
import time

LED_PIN = 11   # You can change this to the pin you connected the LED to

GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)  # Turn LED ON
        time.sleep(1)                    # Wait 1 second
        GPIO.output(LED_PIN, GPIO.LOW)   # Turn LED OFF
        time.sleep(1)                    # Wait 1 second

except KeyboardInterrupt:
    print("Exiting program")
finally:
    GPIO.cleanup()
