# Pico Display - Pimoroni display pack for Raspberry Pi Pico
#
# Prerequisites
#
# Requires Pimoroni MicroPython : https://github.com/pimoroni/pimoroni-pico/blob/main/setting-up-micropython.md

# Import the module for the Display board
import picodisplay as display

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

# SETTING THE LED
# Set the RGB LED.  r,g,b = ints of 0-255.  Effective immediately.
display.set_led(255, 0, 255)


# USING THE SCREEN
# The screen backlight starts at 0.  Must be 0.0-1.0.
display.set_backlight(1.0)

# All drawing actions are done with a pen which defines a colour

# Create pen variables to avoid having to remember what shade the numbers are
black = display.create_pen(0,0,0)
white = display.create_pen(255,255,255)
red = display.create_pen(255,0,0)
green = display.create_pen(0,255,0)
blue = display.create_pen(0,0,255)
purple = display.create_pen(255,0,255)
pink = display.create_pen(255,105,180)
gold = display.create_pen(255,215,0)
orange = display.create_pen(255,140,0)
cyan= display.create_pen(0,255,255)
forestgreen = display.create_pen(34,139,34)
grey = display.create_pen(211,211,211)

# Draw individual characters.  First param is the ASCII number for the char.
# Second and third are top-left X-Y coords.  Optional 4th param is font size,
# defaults to 2/~11px tall/~12 rows, 3 = ~20px/ 5rows, 4 = ~30px/ 4rows

def pico(wait):
    
    display.set_led(255, 0, 255)
    display.set_pen(black)
    display.clear()

    display.set_pen(red)
    display.character(082, 0, 5, 4) # R
    display.set_pen(green)
    display.character(097, 26, 5, 4) # a
    display.set_pen(blue)
    display.character(115, 52, 5, 4) # s
    display.set_pen(purple)
    display.character(112, 78, 5, 4) # p
    display.set_pen(white)
    display.character(098, 104, 5, 4) # b
    display.set_pen(gold)
    display.character(101, 130, 5, 4) # e
    display.set_pen(cyan)
    display.character(114, 156, 5, 4) # r
    display.set_pen(pink)
    display.character(114, 182, 5, 4) # r
    display.set_pen(forestgreen)
    display.character(121, 208, 5, 4) # y

    display.set_pen(cyan)
    display.character(080, 0, 30, 4) # P
    display.set_pen(purple)
    display.character(105, 26, 30, 4) # i

    display.set_pen(white)
    display.character(080, 0, 60, 8) # P
    display.set_pen(orange)
    display.character(105, 45, 60, 8) # i
    display.set_pen(pink)
    display.character(099, 75, 60, 8) # c
    display.set_pen(red)
    display.character(111, 115, 60, 8) # o

    display.update()

while True:                                     # Continuously check for button presses
    if display.is_pressed(display.BUTTON_A):    # Check if the A button is pressed
        display.set_led(255, 255, 255)
        display.set_pen(grey)
        display.clear()
        display.set_pen(black)
        display.text("Button A pressed!", 5, 5, 200)
        display.update()
        
    elif display.is_pressed(display.BUTTON_B):    # Check if the B button is pressed
        display.set_led(0, 0, 255)
        display.set_pen(black)
        display.clear()
        display.set_pen(white)
        display.text("Button B pressed!", 5, 120, 200)
        display.update()
        
    elif display.is_pressed(display.BUTTON_X):    # Check if the X button is pressed
        display.set_led(255, 0, 0)
        display.set_pen(red)
        display.clear()
        display.set_pen(blue)
        display.text("Button X pressed!", 60, 5, 200)
        display.update()
        
    elif display.is_pressed(display.BUTTON_Y):    # Check if the Y button is pressed
        display.set_led(0, 0, 0)
        display.set_pen(cyan)
        display.clear()
        display.set_pen(purple)
        display.text("Button Y pressed!", 60, 120, 200)
        display.update()
        
    else:
        pico(0)
