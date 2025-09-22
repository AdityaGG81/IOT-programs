import RPi.GPIO as GPIO
import time

IR_SENSOR_PIN = 17
LED_PIN = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(IR_SENSOR_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)

print("IR Sensor")

try:
    while True:
        if GPIO.input(IR_SENSOR_PIN) == 0:
            GPIO.output(LED_PIN, GPIO.HIGH)
            print("Obstacle Detected")
        else:
            print("Obstacle Not Detected")
            GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Exiting Program")
finally:
    GPIO.cleanup()
