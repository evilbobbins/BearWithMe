# Raspberry shooter
#
# pressing button A shoots the Raspberry, button B resets the Raspberry
#
# pressing button X increases backlight, button Y decreses backlight
#
# Prerequisites
#
# Pico Display (240x135) - Pimoroni display pack for Raspberry Pi Pico
# Requires Pimoroni MicroPython : https://github.com/pimoroni/pimoroni-pico/blob/main/setting-up-micropython.md

# Import the module for the Display board
import picodisplay as display
import time, random

# INITIAL SETUP
# Initialise the Display board.  This must be done for any features to work.
# Get the width of the display, in pixels (240 pixels)
width = display.get_width()
# Get the height of the display, in pixels (135 pixels)
height = display.get_height()

# Use the above to create a buffer for the screen, 2 bytes per pixel
# (it's a 16bit/RGB565 display, not RGB888)
display_buffer = bytearray(width * height * 2)
# Start the board!
display.init(display_buffer)

# The screen backlight starts at 0.  Must be 0.0-1.0.
bl = 0.5
display.set_backlight(bl)

# Pen colours
red = display.create_pen(255,0,0)
green = display.create_pen(0,255,0)
black = display.create_pen(0,0,0)
white = display.create_pen(255,255,255)

display.set_pen(black)     
display.clear()
    
def raspberry(wait):
    
    display.set_pen(black)
    display.clear()
    
# Raspberry image
    display.set_pen(green) #top

    display.circle(100,30,5)
    display.circle(110,30,5)
    display.circle(120,30,5)
    display.circle(130,30,5)
    display.circle(140,30,5)

    display.circle(110,35,5)
    display.circle(120,35,5)
    display.circle(130,35,5)

    display.circle(110,40,5)
    display.circle(120,40,5)
    display.circle(130,40,5)

    display.circle(120,50,8)

    display.set_pen(red) #berry

    display.circle(110,60,10)
    display.circle(130,60,10)

    display.circle(100,80,10)
    display.circle(120,80,10)
    display.circle(140,80,10)

    display.circle(110,100,10)
    display.circle(130,100,10)

    display.circle(120,120,10)

raspberry(0)
display.update()
    
while True:                                     
    if display.is_pressed(display.BUTTON_A):    # Check if the Y button is pressed
        display.set_led(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        time.sleep(0.01)
        display.circle(random.randint(0, 240), random.randint(0, 240), random.randint(0, 20))
        display.update()
        time.sleep(0.01)
        display.set_led(0,0,0)
        
    if display.is_pressed(display.BUTTON_B):    # Check if the Y button is pressed
        raspberry(0)

        display.update()
        time.sleep(0.1)
        
    if display.is_pressed(display.BUTTON_B):    # Check if the Y button is pressed
        raspberry(0)
        display.update()
        time.sleep(0.1)
        
    if display.is_pressed(display.BUTTON_X):    # Check if the X button is pressed
        bl=bl+0.1
        if bl>1.0:
                  bl=1
        display.set_pen(white)
        display.text("Brightness up!", 50, 60, 200)
        display.set_backlight(bl)
        print(bl)
        display.update()
        time.sleep(0.5)
        raspberry(0)
        display.set_pen(red)
        display.update()
        
    if display.is_pressed(display.BUTTON_Y):    # Check if the Y button is pressed
        bl=bl-0.1
        if bl<0.1:
                bl=0.1
        display.set_pen(white)
        display.text("Brightness down!", 50, 60, 200)
        display.set_backlight(bl)
        print(bl)
        display.update()
        time.sleep(0.5)
        raspberry(0)
        display.set_pen(red)
        display.update()
