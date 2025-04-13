# Based off project 5.1
from gpiozero import RGBLED
from colorzero import Color
import time

led = RGBLED(red="GPIO17", green="GPIO18", blue="GPIO27", active_high=False)

def cleanup():
    led.close()

def main():
    hue = 0
    saturation = 1
    value = 1
    while True:
        hue = (hue + 0.001) % 1
        led.color = Color(h = hue, s = saturation, v = value)

        time.sleep(0.01)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
    finally:
        cleanup()