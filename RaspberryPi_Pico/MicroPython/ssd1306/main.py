# ssd1306 oled display rinning on Raspberry Pi Pico
#
# Prerequisites
#
# Requires Raspberry Pi MicroPython : https://www.raspberrypi.org/documentation/pico/getting-started/
# or
# Requires Pimoroni MicroPython : https://github.com/pimoroni/pimoroni-pico/blob/main/setting-up-micropython.md

# Import the module for the ssd1306

import ssd1306
import machine
import time
import uos
import machine

# display i2c and pico details in thony shell
print(uos.uname())
print("Freq: "  + str(machine.freq()) + " Hz")
print("128x64 SSD1306 I2C OLED on Raspberry Pi Pico")

WIDTH = 128
HEIGHT = 64

i2c = machine.I2C(0)

print("Available i2c devices: "+ str(i2c.scan()))
oled = ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c)
oled.fill(0)

# displays text on display

oled.text("MicroPython", 0, 0)
oled.text("OLED(ssd1306)", 0, 9)
oled.text("-------------------", 0, 20)
oled.text("Dual colour", 0, 30)
oled.text("Rpi Pico", 0, 40)
oled.text("BearWithMe", 0, 50)
oled.show()
