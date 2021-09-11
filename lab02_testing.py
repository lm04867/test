import sys
import time
# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `import grovepi`
sys.path.append('../../Software/Python/')
# This append is to support importing the LCD library.
sys.path.append('../../Software/Python/grove_rgb_lcd')

from grove_rgb_lcd import *
import grovepi

"""This if-statement checks if you are running this python file directly. That
is, if you run `python3 grovepi_sensors.py` in terminal, this if-statement will
be true"""
if __name__ == '__main__':
    ultrasonic = 4    # D4
    lcd_display = 2     #i2c2
    potentiometer = 0   #A0


    while True:
        #So we do not poll the sensors too quickly which may introduce noise,
        #sleep for a reasonable time of 200ms between each iteration.
        time.sleep(0.2)



        distance = grovepi.ultrasonicRead(ultrasonic)
        string_distance = str(distance)
        setText(string_distance)
        setRGB(0,128,64)
