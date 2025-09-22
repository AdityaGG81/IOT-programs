import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
pins=[11,13,15]
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)

try:
    while True:
        for i in range(8):
            binary=format(i,'03b')
            for j in range(3):
                GPIO.output(pins[j], int(binary[j]))
            time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
