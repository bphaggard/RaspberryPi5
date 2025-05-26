import time
from gpiozero import LED

led = LED(17)
user_choice = int(input("Choose 0 to turn LED off or 1 to turn LED on: "))

if user_choice == 1:
    led.on()
elif user_choice == 0:
    led.off()
else:
    print("Wrong number")
    exit()
    
time.sleep(2)
print("END")