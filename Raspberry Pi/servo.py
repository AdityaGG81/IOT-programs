import RPi.GPIO as GPIO
import time

servoPIN = 17   # GPIO pin where the servo signal is connected
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50)  # 50 Hz PWM (standard for servos)
p.start(0)                  # initial duty cycle

def set_angle(angle):
    duty = 2 + (angle / 18)   # Convert angle to duty cycle
    GPIO.output(servoPIN, True)
    p.ChangeDutyCycle(duty)
    time.sleep(0.5)
    GPIO.output(servoPIN, False)
    p.ChangeDutyCycle(0)

try:
    while True:
        # Sweep 0° → 180°
        for angle in range(0, 181, 10):
            set_angle(angle)
            time.sleep(0.2)

        # Sweep 180° → 0°
        for angle in range(180, -1, -10):
            set_angle(angle)
            time.sleep(0.2)

except KeyboardInterrupt:
    print("Exiting program")
    p.stop()
    GPIO.cleanup()
