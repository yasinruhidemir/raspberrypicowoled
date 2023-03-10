
from machine import Pin, SoftI2C
import sh1106
import framebuf
from time import sleep

i2c = machine.SoftI2C(scl=machine.Pin(9), sda=machine.Pin(8)) #Connect i2c defining your scl and sda pins (defaulth is sda = 9 sda = 8)

#Define oled width and height
oled_width = 128 
oled_height = 64

#Initialize the screen
oled = sh1106.SH1106_I2C(oled_width, oled_height, i2c)

oled.fill(0) #Clear the screen
oled.text('Hello, World 1!', 0, 0)  #with oled.text() function you can write a text to the screen
oled.show() #shows the text 
