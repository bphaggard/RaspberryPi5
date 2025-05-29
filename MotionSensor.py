import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)

print("Monitoring GPIO4...")
while True:
    state = GPIO.input(4)
    print("HIGH" if state else "LOW")
    time.sleep(0.1)
