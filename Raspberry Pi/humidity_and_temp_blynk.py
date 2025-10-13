import Adafruit_DHT
import BlynkLib
import time

# Blynk authentication token
BLYNK_AUTH = 'AUTH_TOKEN'

# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH, server="blynk.cloud", port=80)

# Sensor type and GPIO
DHT_SENSOR = Adafruit_DHT.DHT11  # or Adafruit_DHT.DHT22
DHT_PIN = 4

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        print(f"Temp={temperature:.1f}°C  Humidity={humidity:.1f}%")
        blynk.virtual_write(0, temperature)
        blynk.virtual_write(1, humidity)
    else:
        print("Sensor failure. Check wiring.")
    blynk.run()
    time.sleep(2)

