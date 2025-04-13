# Project 5.1
from gpiozero import RGBLED
import time
import random

led = RGBLED(red="GPIO17", green="GPIO18", blue="GPIO27", active_high=False)

def cleanup():
    led.close()

def setColor(red, blue, green):
    led.red = red / 255
    led.green = green / 255
    led.blue = blue / 255

def main():
    while True:
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        setColor(r,g,b)

        print(f"({r}, {g}, {b})")
        time.sleep(1)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
    finally:
        cleanup()