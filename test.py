from gpiozero import LED, Button
import time
from signal import pause

led = LED(17)
button = Button(26)

# while True:
#     time.sleep(0.01)
#     if button.is_pressed:
#         led.on()
#     else:
#         led.off()

button.when_pressed = led.on
button.when_released = led.off

pause()