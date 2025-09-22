import Adafruit_DHT
import time
import requests

# DHT sensor setup
SENSOR = Adafruit_DHT.DHT11  # or Adafruit_DHT.DHT22
PIN = 4  # GPIO pin

# ThingSpeak settings
API_KEY = "YOUR_API_KEY"  # replace with your ThingSpeak write API key
URL = "https://api.thingspeak.com/update"

print("Sending DHT sensor data to ThingSpeak...")

try:
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(SENSOR, PIN)

        if humidity is not None and temperature is not None:
            print(f"Temp={temperature:.1f}°C  Humidity={humidity:.1f}%")

            payload = {
                "api_key": API_KEY,
                "field1": temperature,
                "field2": humidity
            }

            response = requests.get(URL, params=payload)
            if response.status_code == 200:
                print("Data sent to ThingSpeak")
            else:
                print("Failed to send data")

        else:
            print("Sensor failure. Retrying...")

        time.sleep(2)  

except KeyboardInterrupt:
    print("\nStopped by user")