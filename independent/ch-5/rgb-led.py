# Project 5.1 modification
from gpiozero import RGBLED
from colorzero import Color
import time
import random

led = RGBLED(red="GPIO17", green="GPIO18", blue="GPIO27", active_high=False)

def cleanup():
    led.close()

def main():
    while True:
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        led.color = Color(r / 255, g / 255, b / 255)

        print(f"({r}, {g}, {b})")
        time.sleep(1)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
    finally:
        cleanup()