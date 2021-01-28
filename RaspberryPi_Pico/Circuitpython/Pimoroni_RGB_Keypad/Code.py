# Macro keypad - Pimoroni RGB Keypad for Raspberry Pi Pico
# Basics of macro script by https://gist.github.com/sandyjmacdonald
#
# Prerequisites
#
# Requires Adafruit CircuitPython: https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython
#
# Requires the following CircuitPython libs: adafruit_hid, adafruit_bus_device, adafruit_dotstar
# (drop them into the lib folder on Pico)
#
# Save this code in code.py on your Raspberry Pi Pico CIRCUITPY drive
#
# Note that this is specific for macOS and uses button 0 to trigger the macro.

# import setup

import time
import board
import busio
import usb_hid

from adafruit_bus_device.i2c_device import I2CDevice
import adafruit_dotstar as dotstar

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

from digitalio import DigitalInOut, Direction, Pull

# Pull CS pin low to enable level shifter
cs = DigitalInOut(board.GP17)
cs.direction = Direction.OUTPUT
cs.value = 0

# Set up APA102 pixels
num_pixels = 16
pixels = dotstar.DotStar(board.GP18, board.GP19, num_pixels, brightness=0.1, auto_write=True)
pixels_r_0 = [0,1,2,3]

# Set up I2C for IO expander (addr: 0x20)
i2c = busio.I2C(board.GP5, board.GP4)
device = I2CDevice(i2c, 0x20)

# Set up the keyboard
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)


# Function to map 0-255 to position on colour wheel
def colourwheel(pos):
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)


# Read button states from the I2C IO expander on the keypad
def read_button_states(x, y):
    pressed = [0] * 16
    with device:
        # Read from IO expander, 2 bytes (8 bits) correspond to the 16 buttons
        device.write(bytes([0x0]))
        result = bytearray(2)
        device.readinto(result)
        b = result[0] | result[1] << 8

        # Loop through the buttons
        for i in range(x, y):
            if not (1 << i) & b:
                pressed[i] = 1
            else:
                pressed[i] = 0
    return pressed

# List to store the button states
held = [0] * 16

# Colour Chart referance for Colourwheel

    # [0]   # red
    # [10]  # orange
    # [30]  # yellow
    # [85]  # green
    # [137] # cyan
    # [170] # blue
    # [213] # purple

# Visor roll animation

def pixels_r_0_0(wait):
        pixels[0] = colourwheel(0)
        pixels[1] = colourwheel(0)
        pixels[2] = colourwheel(0)
        pixels[3] = colourwheel(0)
        time.sleep(0.2)

def pixels_r_1_85(wait):
        pixels[4] = colourwheel(85)
        pixels[5] = colourwheel(85)
        pixels[6] = colourwheel(85)
        pixels[7] = colourwheel(85)
        time.sleep(0.2)

def pixels_r_2_170(wait):
        pixels[8] = colourwheel(170)
        pixels[9] = colourwheel(170)
        pixels[10] = colourwheel(170)
        pixels[11] = colourwheel(170)
        time.sleep(0.2)

def pixels_r_3_213(wait):
        pixels[12] = colourwheel(213)
        pixels[13] = colourwheel(213)
        pixels[14] = colourwheel(213)
        pixels[15] = colourwheel(213)
        time.sleep(0.2)

def pixels_r_0_213(wait):
        pixels[0] = colourwheel(213)
        pixels[1] = colourwheel(213)
        pixels[2] = colourwheel(213)
        pixels[3] = colourwheel(213)
        time.sleep(0.2)

def pixels_r_1_170(wait):
        pixels[4] = colourwheel(170)
        pixels[5] = colourwheel(170)
        pixels[6] = colourwheel(170)
        pixels[7] = colourwheel(170)
        time.sleep(0.2)

def pixels_r_2_85(wait):
        pixels[8] = colourwheel(85)
        pixels[9] = colourwheel(85)
        pixels[10] = colourwheel(85)
        pixels[11] = colourwheel(85)
        time.sleep(0.2)

def pixels_r_3_0(wait):
        pixels[12] = colourwheel(0)
        pixels[13] = colourwheel(0)
        pixels[14] = colourwheel(0)
        pixels[15] = colourwheel(0)
        time.sleep(0.2)

# Shortcode to run animation 

def loadingflash(wait):
    for i in range(2):

        pixels_r_0_0(0)
        pixels_r_1_85(0)
        pixels_r_2_170(0)
        pixels_r_3_213(0)
        pixels_r_3_0(0)
        pixels_r_2_85(0)
        pixels_r_1_170(0)
        pixels_r_0_213(0)


    for i in range(2):
        pixels.fill((0, 255, 0))
        time.sleep(0.5)

# Play animation on boot

loadingflash(0)

# Macros on keypad button press

# Keypad layout referance
#   Row3 Row2 Row1 Row0
#   [12] [ 8] [ 4] [ 0]
#   [13] [ 9] [ 5] [ 1]
#   [14] [10] [ 6] [ 2]
#   [15] [11] [ 7] [ 3]

while True:

    pressed = read_button_states(0, 16)

# Row0

    if pressed[0]:
        pixels[0] = colourwheel(0)  # Map pixel index to 0-255 range

        if not held[0]:

            # Trigger Spotlight search
            kbd.send(Keycode.COMMAND, Keycode.SPACE)
            time.sleep(0.2)

            # Open Safari
            layout.write("safari")
            time.sleep(0.1)
            kbd.send(Keycode.ENTER)
            time.sleep(0.5)

            # Focus on search bar
            kbd.send(Keycode.COMMAND, Keycode.L)
            time.sleep(0.1)

            # Go to Google.com
            layout.write("https://google.com")
            time.sleep(0.2)
            kbd.send(Keycode.ENTER)

            # Update held state to prevent retriggering
            held[0] = 1

    if pressed[1]:
        pixels[1] = colourwheel(0)  # Map pixel index to 0-255 range

        if not held[1]:
            # Trigger Spotlight search
            kbd.send(Keycode.COMMAND, Keycode.SPACE)
            time.sleep(0.2)

            # Open Safari
            layout.write("safari")
            time.sleep(0.1)
            kbd.send(Keycode.ENTER)
            time.sleep(0.5)

            # New Tab
            kbd.send(Keycode.COMMAND, Keycode.T)
            time.sleep(0.2)

            # Focus on search bar
            kbd.send(Keycode.COMMAND, Keycode.L)
            time.sleep(0.1)

            # Go to youtube
            layout.write("https://youtube.com")
            time.sleep(0.2)
            kbd.send(Keycode.ENTER)

            # Update held state to prevent retriggering
            held[1] = 1

    if pressed[2]:
        pixels[2] = colourwheel(0)  # Map pixel index to 0-255 range

        if not held[2]:
            # Trigger Spotlight search
            kbd.send(Keycode.COMMAND, Keycode.SPACE)
            time.sleep(0.2)

            # Open Safari
            layout.write("safari")
            time.sleep(0.1)
            kbd.send(Keycode.ENTER)
            time.sleep(0.5)

            # New Tab
            kbd.send(Keycode.COMMAND, Keycode.T)
            time.sleep(0.2)

            # Focus on search bar
            kbd.send(Keycode.COMMAND, Keycode.L)
            time.sleep(0.1)

            # Go to Github
            layout.write("https://github.com")
            time.sleep(0.2)
            kbd.send(Keycode.ENTER)

            # Update held state to prevent retriggering
            held[2] = 1

    if pressed[3]:
        pixels[3] = colourwheel(0)  # Map pixel index to 0-255 range

        if not held[2]:
            # Trigger Spotlight search
            kbd.send(Keycode.COMMAND, Keycode.SPACE)
            time.sleep(0.2)

            # Open Safari
            layout.write("safari")
            time.sleep(0.1)
            kbd.send(Keycode.ENTER)
            time.sleep(0.5)

            # New Tab
            kbd.send(Keycode.COMMAND, Keycode.T)
            time.sleep(0.2)

            # Focus on search bar
            kbd.send(Keycode.COMMAND, Keycode.L)
            time.sleep(0.1)

            # Go to Github
            layout.write("https://www.raspberrypi.org")
            time.sleep(0.2)
            kbd.send(Keycode.ENTER)

            # Update held state to prevent retriggering
            held[2] = 1

    if pressed[4]:
        pixels[4] = colourwheel(85)  # Map pixel index to 0-255 range

        if not held[4]:
            # Trigger Spotlight search
            kbd.send(Keycode.COMMAND, Keycode.SPACE)
            time.sleep(0.2)

            # Open Safari
            layout.write("calculator")
            time.sleep(0.1)
            kbd.send(Keycode.ENTER)
            time.sleep(0.5)

            # Update held state to prevent retriggering
            held[4] = 1
# Row1

    if pressed[5]:
        pixels[5] = colourwheel(137)  # Map pixel index to 0-255 range

        if not held[5]:
            # Trigger Spotlight search
            kbd.send(Keycode.COMMAND, Keycode.SPACE)
            time.sleep(0.2)

            # Open terminal
            layout.write("terminal")
            time.sleep(0.1)
            kbd.send(Keycode.ENTER)
            time.sleep(0.5)

            # Update held state to prevent retriggering
            held[5] = 1

# Row2

    if pressed[11]:
        pixels[11] = colourwheel(213)  # Map pixel index to 0-255 range

        if not held[11]:

            # Type Text
            layout.write("Random Text")
            time.sleep(0.1)
            kbd.send(Keycode.ENTER)
            time.sleep(0.5)

            # Update held state to prevent retriggering
            held[11] = 1

# Row3
            
    if pressed[12]:
        pixels[12] = colourwheel(170)  # Map pixel index to 0-255 range

        if not held[12]:
            # Trigger Spotlight search
            kbd.send(Keycode.COMMAND, Keycode.SPACE)
            time.sleep(0.2)

            # Open Safari
            layout.write("safari")
            time.sleep(0.1)
            kbd.send(Keycode.ENTER)
            time.sleep(0.5)

            # New Tab
            kbd.send(Keycode.COMMAND, Keycode.T)
            time.sleep(0.2)

            # Focus on search bar
            kbd.send(Keycode.COMMAND, Keycode.L)
            time.sleep(0.1)

            # Go to Local Plex Server
            layout.write("http://192.168.1.200:32400/web/index.html")
            time.sleep(0.2)
            kbd.send(Keycode.ENTER)

            # Update held state to prevent retriggering
            held[12] = 1



    if pressed[15]:
        pixels[15] = colourwheel(250)  # Map pixel index to 0-255 range

        if not held[15]:

            # Update held state to prevent retriggering
            held[15] = 1
            pixels[15] = (0, 0, 0)  # Turn pixel off

            # Type Text
            loadingflash(0)

    else:  # Released Button state and turn off

        pixels[0] = (0, 0, 0)  # Turn pixel off
        held[0] = 0  # Set held state to off
        pixels[1] = (0, 0, 0)  # Turn pixel off
        held[1] = 0  # Set held state to off
        pixels[2] = (0, 0, 0)  # Turn pixel off
        held[2] = 0  # Set held state to off
        pixels[3] = (0, 0, 0)  # Turn pixel off
        held[3] = 0  # Set held state to off

        pixels[4] = (0, 0, 0)  # Turn pixel off
        held[4] = 0  # Set held state to off
        pixels[5] = (0, 0, 0)  # Turn pixel off
        held[5] = 0  # Set held state to off
        pixels[6] = (0, 0, 0)  # Turn pixel off
        held[6] = 0  # Set held state to off
        pixels[7] = (0, 0, 0)  # Turn pixel off
        held[7] = 0  # Set held state to off

        pixels[8] = (0, 0, 0)  # Turn pixel off
        held[8] = 0  # Set held state to off
        pixels[9] = (0, 0, 0)  # Turn pixel off
        held[9] = 0  # Set held state to off
        pixels[10] = (0, 0, 0)  # Turn pixel off
        held[10] = 0  # Set held state to off
        pixels[11] = (0, 0, 0)  # Turn pixel off
        held[11] = 0  # Set held state to off

        pixels[12] = (0, 0, 0)  # Turn pixel off
        held[12] = 0  # Set held state to off
        pixels[13] = (0, 0, 0)  # Turn pixel off
        held[13] = 0  # Set held state to off
        pixels[14] = (0, 0, 0)  # Turn pixel off
        held[14] = 0  # Set held state to off
        pixels[15] = (0, 0, 0)  # Turn pixel off
        held[15] = 0  # Set held state to off
