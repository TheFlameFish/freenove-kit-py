# Project 4.1
from gpiozero import PWMLED
import time

led = PWMLED("GPIO18", initial_value= 0.0, frequency=1000)

def cleanup():
    led.close()

def main():
    while True:
        for i in range(0, 101, 1):
            led.value = i / 100 # Between 0.0 & 1.0
            time.sleep(0.01)
        time.sleep(1.0)
        for i in range(100, -1, -1):
            led.value = i / 100
            time.sleep(0.01)
        time.sleep(0) # Remove the delay because I like the way that looks

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting.")
    finally:
        cleanup()