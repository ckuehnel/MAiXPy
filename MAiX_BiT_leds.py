# Controlling Internal LEDS

from Maix import GPIO
from utime import *

# Red LED
fm.register(board_info.LED_R, fm.fpioa.GPIO0)
led_r=GPIO(GPIO.GPIO0,GPIO.OUT)
led_r.value(1)

# Green LED 
fm.register(board_info.LED_G, fm.fpioa.GPIO1)
led_g=GPIO(GPIO.GPIO1,GPIO.OUT)
led_g.value(1)

# Blue LED
fm.register(board_info.LED_B, fm.fpioa.GPIO2)
led_b=GPIO(GPIO.GPIO2,GPIO.OUT)
led_b.value(1)

while True:
	led_r.value(0)
	sleep_ms(500)
	led_r.value(1)
	led_g.value(0)
	sleep_ms(500)
	led_g.value(1) 
	led_b.value(0)
	sleep_ms(500)
	led_b.value(1)