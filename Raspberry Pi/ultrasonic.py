import RPi.GPIO as GPIO
import time

# Pin setup
TRIG = 23   # GPIO pin for Trigger
ECHO = 24   # GPIO pin for Echo

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

print("Ultrasonic Sensor Measurement")

try:
    while True:
        # Ensure trigger is low
        GPIO.output(TRIG, False)
        time.sleep(0.5)

        # Send a 10us pulse to trigger
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        # Wait for echo start
        while GPIO.input(ECHO) == 0:
            pulse_start = time.time()

        # Wait for echo end
        while GPIO.input(ECHO) == 1:
            pulse_end = time.time()

        # Calculate distance
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150  # speed of sound (34300 cm/s) / 2
        distance = round(distance, 2)

        print("Distance:", distance, "cm")

except KeyboardInterrupt:
    print("Exiting program")

finally:
    GPIO.cleanup()
