from gpiozero import LED, Button
from signal import pause

led_list = [LED(17), LED(27), LED(22)]
button = Button(26, bounce_time=0.05) #bounce_time prevent code to think that button was pressed twice
led_index = 0

def switch_led_off():
    for led in led_list:
        led.off()

def switch_led():
    global led_index
    switch_led_off()
    led_list[led_index].on()
    led_index = (led_index + 1) % len(led_list)

switch_led_off()
button.when_pressed = switch_led
pause()