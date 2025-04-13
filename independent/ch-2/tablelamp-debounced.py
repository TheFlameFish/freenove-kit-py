# Project 2.2 but debounced
# They talked about debouncing in the project intro but then didn't
# implement it for some reason
from gpiozero import LED, Button
import time

led = LED("GPIO17")
button = Button("GPIO18", pull_up= True, bounce_time=0.05)

def onButtonPressed():
    led.toggle()
    if led.is_active:
        print("LED turned on.")
    else:
        print("LED turned off.")

def destroy():
    led.close()
    button.close()

def main():
    button.when_activated = onButtonPressed
    while True:
        time.sleep(1)

if __name__ == '__main__':
    print("Starting tablelamp.")
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting program.")
    finally:
        destroy()