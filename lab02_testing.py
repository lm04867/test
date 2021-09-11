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

    grovepi.pinMode(ultrasonic, "OUTPUT")

    i = 0
    while True:
        #So we do not poll the sensors too quickly which may introduce noise,
        #sleep for a reasonable time of 200ms between each iteration.
        time.sleep(0.2)

        #Reads a number between 0-1023 and divides it to have same range as ultrasonic reader
        i = grovepi.analogRead(potentiometer)
        threshold = i/1.978723
        string_threshold = str(threshold)
        print(threshold)


        #Reads ultrosonic data between 0-517 then stores in variable
        distance = grovepi.ultrasonicRead(ultrasonic)

        #converts int to string to it can be displayed on lcd
        string_distance = str(distance)

        if distance < threshold:
            #Object present


            setText(string_threshold + "OBJ PRES \n" + string_distance)
            setRGB(0,128,64)
