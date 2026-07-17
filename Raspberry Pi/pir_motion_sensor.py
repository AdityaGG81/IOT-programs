import RPi.GPIO as GPIO
import time

# Pin setup
PIR_PIN = 17   # GPIO pin for PIR sensor
LED_PIN = 27   # GPIO pin for LED (optional, for feedback)

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)

print("PIR Motion Sensor Started")
print("Waiting for sensor to stabilize...")
time.sleep(2)

motion_detected = False

try:
    while True:
        if GPIO.input(PIR_PIN) == GPIO.HIGH:
            if not motion_detected:
                print("Motion detected!")
                GPIO.output(LED_PIN, GPIO.HIGH)  # Turn LED ON
                motion_detected = True
        else:
            if motion_detected:
                print("No motion")
                GPIO.output(LED_PIN, GPIO.LOW)   # Turn LED OFF
                motion_detected = False
        
        time.sleep(0.5)

except KeyboardInterrupt:
    print("Exiting program")
finally:
    GPIO.output(LED_PIN, GPIO.LOW)
    GPIO.cleanup()
