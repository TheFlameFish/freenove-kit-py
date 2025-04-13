# Project 6.1
from gpiozero import Buzzer, Button
import time

buzzer = Buzzer("GPIO17")
button = Button("GPIO18", bounce_time=0.05) # Added debouncing

def cleanup():
    buzzer.close()
    button.close()

def onButtonPressed():
    buzzer.on()
    print("Button pressed. Buzzer enabled")

def onButtonReleased():
    buzzer.off()
    print("Button released. Buzzer disabled")

def main():
    button.when_activated = onButtonPressed
    button.when_deactivated = onButtonReleased
    while True:
        time.sleep(1)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        cleanup()