import RPi.GPIO as GPIO
import time;
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)

binary_states = [(0,0),
                 (0,1),
                 (1,0),
                 (1,1)]

try:
    while True:
        for i in range(4):
            binary = format(i, '02b')
            GPIO.output(11,int(binary[0]))
            GPIO.output(13,int(binary[1]))
            time.sleep(1.0)
except KeyboardInterrupt:
    GPIO.cleanup()
