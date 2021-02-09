# Bouncing Pixel Heart
#
# Prerequisites
#
# Pico Display (240x135) - Pimoroni display pack for Raspberry Pi Pico
# Requires Pimoroni MicroPython : https://github.com/pimoroni/pimoroni-pico/blob/main/setting-up-micropython.md

# Import the module for the Display board
import picodisplay as display
import time

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
brightwhite = display.create_pen(255,255,255)
white =  display.create_pen(155,155,155)   
skyblue = display.create_pen(50,50,115)

heartgrid=["00111000000011100","01222100000122210","12222210001222221","12222221112222221","12222222222222221","01222222222222210","00122222222222100","00012222222221000","00001222222210000","00000122222100000","00000012221000000","00000001210000000","00000000100000000","00000000000000000"]

def drawheart(x,y,zoom):
    #draw the heart
    row = 0
    col = 0
    for line in heartgrid:
        #print(line)
        for pixel in line:
            #print(pixel)
            colour = str(pixel)
            if colour != "0":
                if colour == "1":
                    display.set_pen(black)
                if colour == "2":
                    display.set_pen(red)
                display.rectangle(x+(col*zoom),y+(row*zoom),zoom,zoom)
            col+=1
        row+=1
        col=0

class Heart:
    def __init__(self, x,y):
        self.x = x 
        self.y = y
        self.edge_reached = False

def heartbeat():
    display.set_led(255,0,0)
    time.sleep(0.1)
    display.set_led(0,0,0)
    time.sleep(0.1)
    display.set_led(255,0,0)
    time.sleep(0.1)
    display.set_led(0,0,0)
    time.sleep(0.1)
        
heart = Heart(0,20)

print("Bouncing Pixel Heart")

while True:
    display.set_pen(skyblue)    
    display.clear()
    
    drawheart(heart.x,heart.y,8)
    #print("Heart X = ",heart.x)
    
    if not heart.edge_reached:
            heart.x -= 1
            if heart.x <= 0:
                heart.edge_reached=True
                heartbeat()
                print("Right Edge Reached = ",heart.edge_reached)
        
    else:
        if  heart.edge_reached:
            heart.x += 1
            if heart.x >= width-135:
                heart.edge_reached=False
                heartbeat()
                print("Right Edge Reached = ",heart.edge_reached)
        
    display.update()


