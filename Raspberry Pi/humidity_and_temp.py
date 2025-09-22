import Adafruit_DHT
import time

# DHT sensor setup
SENSOR = Adafruit_DHT.DHT11   # or Adafruit_DHT.DHT22
PIN = 4                       # GPIO pin

print("Reading DHT sensor data...")

try:
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(SENSOR, PIN)

        if humidity is not None and temperature is not None:
            print(f"Temp={temperature:.1f}°C  Humidity={humidity:.1f}%")
        else:
            print("Sensor failure. Retrying...")

        time.sleep(2)

except KeyboardInterrupt:
    print("\nStopped by user")
