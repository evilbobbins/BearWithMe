# Bouncing berry
#
# Prerequisites
#
# Pico Display (240x135) - Pimoroni display pack for Raspberry Pi Pico
# Requires Pimoroni MicroPython : https://github.com/pimoroni/pimoroni-pico/blob/main/setting-up-micropython.md

import time, random
import picodisplay as display 

# INITIAL SETUP
# Initialise the Display board.  This must be done for any features to work.
# Get the width of the display, in pixels (240 pixels)
width = display.get_width()
# Get the height of the display, in pixels (135 pixels)
height = display.get_height()
display_buffer = bytearray(width * height * 2)  # Screen Buffer 2-bytes per pixel (RGB565)
display.init(display_buffer)

# The screen backlight starts at 0.  Must be 0.0-1.0.
display.set_backlight(1.0)

#colours
red = display.create_pen(255,0,0)
green = display.create_pen(0,255,0)
black = display.create_pen(0,0,0)

berrygrid=["00000011111100000000111111000000","0000013333310000001333333100000","00011333333331100113333333311000","01133333333333311333333333333110","13333333333333311333333333333331","01333311333333111133333311333310","00133333111133111133111133333100","00013333333111111111133333331000","00001133333111111111133333110000","00000013331111222211113331000000","00000111111112222221111111100000","00001122211122222222111222110000","00001222211122222222111222210000","00011222111122222222111122211000","00111221222112222221122212211100","00121112222211222211222221112100","01222122222221111112222222122210","01222122222221111112222222122210","01222122222221111112222222122210","01222112222211222211222221122210","01222111222112222221122211122210","00121111111122222222111111112100","00111122111122222222111122111100","00011222211122222222111222211000","00001222221112222221112222210000","00001222222111222211122222210000","00000122222111111111122222100000","00000012221112222221112221000000","00000001111122222222111110000000","00000000011122222222111000000000","00000000000112222221100000000000","00000000000001111110000000000000"]


def drawberry(x,y,r):
    #draw the heart
    x=int(x)
    y=int(y)
    r=2
    row = 0
    col = 0
    for line in berrygrid:
        #print(line)
        for pixel in line:
            #print(pixel)
            colour = str(pixel)
            if colour != "0":
                if colour == "1":
                    display.set_pen(black)
                if colour == "2":
                    display.set_pen(red)
                if colour == "3":
                    display.set_pen(green)
                display.rectangle(x+(col*r),y+(row*r),r,r)
            col+=1
        row+=1
        col=0

class berry:
    def __init__(self, x, y, r, dx, dy):
        self.x = x 
        self.y = y
        self.r = r
        self.dx = dx
        self.dy = dy
        
berrys = []
for i in range(0, 1): # amount of berrys
    berrys.append(
        berry(
            random.randint(0, 20),
            random.randint(0, 20),
            random.randint(0, 10) + 3,
            random.randint(0, 255) / 128,
            random.randint(0, 255) / 128,
            
        )
    )
    
print("Bouncing Pixel Raspberry")  

while True:
    display.set_pen(0, 0, 0)    
    display.clear()
    
    for berry in berrys:        
        berry.x += berry.dx
        berry.y += berry.dy
        
        
        if berry.x < 0 or berry.x > 180:
            berry.dx *= -1
        if berry.y < 0 or berry.y > 68:
            berry.dy *= -1
            
        drawberry((berry.x), int(berry.y), int(berry.r))
            
        display.update() 
